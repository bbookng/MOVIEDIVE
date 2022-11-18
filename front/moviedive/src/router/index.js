import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import LogoutView from '@/views/LogoutView.vue'
import MainView from '@/views/MainView'
import CollectionsView from '@/views/CollectionsView'
import CommunityView from '@/views/CommunityView'
import PlayView from '@/views/PlayView'
import DeepDiveView from '@/views/DeepDiveView'
import MyPageView from '@/views/MyPageView'
import ReviewFormView from '@/views/ReviewFormView'
// import CollectionDetailView from '@/views/CollectionDetailView'
import SearchResultView from '@/views/SearchResultView'
import CollectionCreationFormView from '@/views/CollectionCreationFormView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView

  },
  {
    path: '/collection',
    name: 'collection',
    component: CollectionsView
  },
  // community
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/review_detail/:movieId/:reviewId',
    name: 'review_detail',
    component: () => import('@/views/ReviewDetailView')
  },
  {
    path: '/review/create',
    name: 'create_review',
    component: ReviewFormView
  },
  {
    path: '/play',
    name: 'play',
    component: PlayView
  },
  {
    path: '/deepdive',
    name: 'deepdive',
    component: DeepDiveView
  },
  {
    path: '/mypage/:username',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/collection/create/',
    name: 'create_collection',
    component: CollectionCreationFormView
  },
  {
    path: '/search/:keyword/',
    name: 'search_result',
    component: SearchResultView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// Navigation Guard 설정
router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn && to.name !== 'main') {
    alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (to.name == 'main') {
    next({ name: 'main' })
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'main' })
  }
})

export default router
