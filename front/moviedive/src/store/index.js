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
    createPersistedState({
      key: 'vuex',
      reducer(val) {
        if (val.isLoggedIn === false) {
          return {}
        }
        return val
      }
    }),
  ],
  state: {
    token: localStorage.getItem('token') || '',
    movies: [],
    movie: {},
    suggests: [],
    reviews: [],
    currentUser: {},
    collections: [],
    newmovielist: [],
    authError: null,
    API_URL: 'http://127.0.0.1:8000/api',
    collection: [],
    mypage: 1,
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    // searched_movies: state => state.searched_movies,
    suggests: state => state.suggests,
    isLoggedIn(state) {
      return state.token ? true : false
    },
    collections: state => state.collections,
    currentUser: state => state.currentUser,
    authHeader: state => ({ Authorization: `Token ${state.token}` }),
    authError: state => state.authError,
    newmovielist: state => state.newmovielist,
    collection: state => state.collection,
  },
  mutations: {
    // 회원가입 && 로그인
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    GET_COLLECTIONS(state, collections) {
      state.collections = collections
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_SUGGESTS: (state, suggests) => state.suggests = suggests,
    SET_NEW_MOVIE_LIST: (state, movies) => state.newmovielist = movies,
    GET_MY_PAGE: (state, flag) => state.mypage = flag,
    GET_PROFILE_MODIFY: (state, flag) => state.mypage = flag,
    GET_ACCOUNT_MODIFY: (state, flag) => state.mypage = flag,
  },
  actions: {
    signUp({ dispatch, commit }, credentials) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: credentials,
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'main' })
        })
        .then(() => {
          console.log(credentials.nickname)
          dispatch('setNickname', credentials.nickname)
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    setNickname(context, nickname) {
      console.log(nickname)
      console.log(drf.accounts.set_nickname)
      axios({
        method: 'put',
        url: 'http://localhost:8000/api/accounts/profile/set_nickname/',
        headers: context.getters.authHeader,
        data: {
          nickname: nickname
        }
      })
        .then((res) => {
          console.log(res)
        })
    },
    logIn({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 login URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'main' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    saveToken({ commit }, token) {
      /* 
      state.token 추가 
      localStorage에 token 추가
      */
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },
    logout({ dispatch }) {
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
        // headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          router.push({ name: 'main' })
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
        .then((res) => {
          context.commit('GET_COLLECTIONS', res.data)
        })
    },
    fetchMovies({ commit, getters }, keyword) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */

      let query = "?"
      if (keyword) {
        query += `keyword=${keyword}`
      }

      axios({
        url: `http://127.0.0.1:8000/movies/search/` + query,
        // url: `http://127.0.0.1:8000/movies/search/${keyword}/`,
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit(`SET_MOVIES`, res.data)
        })
        .catch(err => console.error(err.response))
    },
    fetchMovie({ commit, getters }, movieId) {
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
        url: drf.movies.movie(movieId),
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
    autoComplete({ commit, getters }, keyword) {
      commit('SET_SUGGESTS', [])
      axios({
        url: drf.movies.auto_complete(keyword),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SUGGESTS', res.data)
        })
    },
    deleteSuggestion({ commit }) {
      commit('SET_SUGGESTS', [])
    },
  },

  modules: {
  }
})
