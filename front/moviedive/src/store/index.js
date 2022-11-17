import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/api'

export default new Vuex.Store({
  state: {
    token: null,
    movies: [],
    currentUser: {},
  },
  getters: {  
    isLoggedIn(state) {
      return state.token ? true : false
    },
    currentUser: state => state.currentUser,
  },
  mutations: {
      // 회원가입 && 로그인
      SAVE_TOKEN(state, token) {
        state.token = token
        router.push({ name: 'main' })
      },
      GET_MOVIES(state, movies) {
        state.movies = movies
      },
      SET_CURRENT_USER: (state, user) => state.currentUser = user,
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
          email: payload.email,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(() => alert('이미 있다'))
    },
    getNickname(context, nickname) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/setnickname/`,
        data: {
          nickname: nickname
        }
      })
      .then((res) => {
        console.log(res)
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
    // logout({ getters, dispatch }) {
    //   axios({
    //     url: `${API_URL}/accounts/logout/`,
    //     method: 'post',
    //     // data: {},
    //     headers: getters.authHeader,
    //   })
    //     .then(() => {
    //       dispatch('removeToken')
    //       router.push({ name: 'login' })
    //     })
    //     .error(err => {
    //       console.error(err.response)
    //     })
    // },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then(res => 
        context.commit('GET_MOVIES', res.data))
    },
    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
      if (getters.isLoggedIn) {
        axios({
          url: `${API_URL}/accounts/currentuser/`,
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_CURRENT_USER', res.data)
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },
  },
  modules: {
  }
})
