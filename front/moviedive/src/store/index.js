import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/api'

export default new Vuex.Store({
  state: {
    token: null,
    movies: []
  },
  getters: {  
  },
  mutations: {
      // 회원가입 && 로그인
      SAVE_TOKEN(state, token) {
        state.token = token
        router.push({ name: 'ArticleView' })
      },
      GET_MOVIES(state, movies) {
        state.movies = movies
      }
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then(res => 
        context.commit('GET_MOVIES', res.data))
    }
  },
  modules: {
  }
})
