import React, { useEffect } from "react";
import ReactDOM from "react-dom";
import { createStore, applyMiddleware, combineReducers } from "@reduxjs/toolkit";
import { Provider, useSelector, useDispatch } from "react-redux";
import thunk from "redux-thunk";
import axios from "axios";
import { List, Card } from "antd";
import "antd/dist/antd.css";


const pokemonSlice = createSlice({
  name: "pokemon",
  initialState: { data: [], loading: false },
  reducers: {
    fetchStart: (state) => {
      state.loading = true;
    },
    fetchSuccess: (state, action) => {
      state.data = action.payload;
      state.loading = false;
    },
    fetchError: (state) => {
      state.loading = false;
    },
  },
});


const { fetchStart, fetchSuccess, fetchError } = pokemonSlice.actions;


const rootReducer = combineReducers({ pokemon: pokemonSlice.reducer });
const store = createStore(rootReducer, applyMiddleware(thunk));


const fetchPokemon = () => async (dispatch) => {
  dispatch(fetchStart());
  try {
    const response = await axios.get("https://pokeapi.co/api/v2/pokemon?limit=20");
    const results = response.data.results;
    const sprites = await Promise.all(
      results.map(async (result) => {
        const details = await axios.get(result.url);
        return details.data.sprites.front_default;
      })
    );
    dispatch(fetchSuccess(sprites));
  } catch (error) {
    dispatch(fetchError());
  }
};


const App = () => {
  const dispatch = useDispatch();
  const pokemon = useSelector((state) => state.pokemon);


  useEffect(() => {
    dispatch(fetchPokemon());
  }, [dispatch]);


  return (
    <List
      grid={{ gutter: 16, column: 4 }}
      dataSource={pokemon.data}
      renderItem={(item) => (
        <List.Item>
          <Card style={{ width: 120 }} cover={<img alt="pokemon" src={item} />} />
        </List.Item>
      )}
    />
  );
};


ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);
