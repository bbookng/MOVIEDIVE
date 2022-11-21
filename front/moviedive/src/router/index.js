import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import LogoutView from '@/views/LogoutView'

import DiveView from '@/views/DiveView'
import MainView from '@/views/MainView'
import CollectionsView from '@/views/CollectionsView'
import CommunityView from '@/views/CommunityView'
import PlayView from '@/views/PlayView'
import DeepDiveView from '@/views/DeepDiveView'
import MyPageView from '@/views/MyPageView'
import ReviewFormView from '@/views/ReviewFormView'
import SearchResultView from '@/views/SearchResultView'
import CollectionDetailView from '@/views/CollectionDetailView'
import CollectionCreationFormView from '@/views/CollectionCreationFormView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'dive',
    component: DiveView
  },
  {
    path: '/main',
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
    path: '/collection/:collectionPk',
    name: 'collection_detail',
    component: CollectionDetailView
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
    path: '/search/:keyword/',
    name: 'search_result',
    component: SearchResultView
  },
  {
    path: '/collection/save/',
    name: 'save_collection',
    component: CollectionCreationFormView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
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
