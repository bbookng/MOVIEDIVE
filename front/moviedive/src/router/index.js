import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MainView from '@/views/MainView'
import CollectionsView from '@/views/CollectionsView'
import CommunityView from '@/views/CommunityView'
import PlayView from '@/views/PlayView'
import DeepDiveView from '@/views/DeepDiveView'
import MyPageView from '@/views/MyPageView'
import ReviewCreateView from '@/views/ReviewCreateView'

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
    path: '/review-detail/:movieId/:reviewId',
    name: 'review-detail',
    component: () => import('@/views/ReviewDetailView')
  },
  {
    path: '/review-create',
    name: 'review-create',
    component: ReviewCreateView
  },
  //
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
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
