<template>
    <div class="login-section">
      <section class="vh-100">
          <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
              <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                <div class="card bg-white text-dark" style="border-radius: 1rem;">
                  <div class="card-body p-5 text-center">
                  <div class="mb-md-5 mt-md-4 pb-5">
                      <h2 class="fw-bold mb-2 text-uppercase">무비다이브로 로그인</h2>
                      <p class="text-gray-50 mb-5">숨 참고 MOVIEDIVE</p>
                      <div class="form-outline form-white mb-4">
                        <input v-model="username" placeholder="아이디" type="text" id="username" class="form-control form-control-lg" />
                      </div>
                      <div class="form-outline form-white mb-4">
                        <input v-model="password" placeholder="비밀번호" type="password" id="password" class="form-control form-control-lg" />
                    </div>
                    <form @submit.prevent="logIn">
                      <button class="btn btn-light btn-lg px-5" type="submit">로그인</button>
                    </form>
                  </div>
              <div>
                <p class="mb-0">아이디가 없다면? 무비다이브와 함께하세요! 👉🏼 <router-link :to="{ name: 'signup' }" style="text-decoration:none; color:#7830DC;">회원가입</router-link></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style scoped>

.login-section {
  width: 100%;
  height: 100%;
}
</style>