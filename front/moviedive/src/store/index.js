import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import drf from '@/api/drf'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/api'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: localStorage.getItem('token') || '' ,
    movies: [],
    reviews: [],
    currentUser: {},
    collections: [],
    authError: null,
  },
  getters: {
    movies: state => state.movies,  
    isLoggedIn(state) {
      return state.token ? true : false
    },
    currentUser: state => state.currentUser,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    authError: state => state.authError,
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
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    GET_COLLECTIONS(state, collections) {
      state.collections = collections
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
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
    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },
    logout({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          router.push({ name: 'login' })
        })
        .error(err => {
          console.error(err.response)
        })
    },
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
    getCollections(context) {
      axios({
        method: 'GET',
        url: `${API_URL}/collections/`,
      })
      .then((res)=>{
        context.commit('GET_COLLECTIONS', res.data)
      })
    },
    getReviews(context) {
      axios({
        method: 'get',
        url: `${API_URL}/community/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, context)
          // console.log(res.data)
          context.commit('GET_REVIEWS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    
    fetchMovie({ commit, getters }, moviePk) {
      /* 영화 정보 1개 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 정보를 state.movie에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE', res.data)
        })
          
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
  },
  modules: {
  }
})
