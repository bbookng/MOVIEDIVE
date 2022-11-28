<template>
  <div class="signup-section">
    <section class="vh-100">
          <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
              <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                <div class="card bg-white text-dark" style="border-radius: 1rem;">
                  <div class="card-body p-5 text-center">
                  <div class="mb-md-5 mt-md-4 pb-5">
                      <h2 class="fw-bold mb-2 text-uppercase">무비다이브에서 놀기</h2>
                      <p class="text-gray-50 mb-5">가입하고 다양한 서비스를 마음껏 즐기세요!</p>
                      <div class="form-outline form-white mb-4">
                        <input v-model="username" placeholder="아이디" type="text" id="username" class="form-control form-control-lg" />
                      </div>
                      <div class="form-outline form-white mb-4">
                        <input v-model="password1" placeholder="비밀번호" type="password" id="password1" class="form-control form-control-lg" />
                      </div>
                      <div class="form-outline form-white mb-4">
                        <input v-model="password2" placeholder="비밀번호를 한 번 더 입력해주세요." type="password" id="password2" class="form-control form-control-lg" />
                      </div>
                      <div class="form-outline form-white mb-4">
                        <input v-model="email" placeholder="이메일" type="email" id="email" class="form-control form-control-lg" />
                      </div>
                      <div class="form-outline form-white mb-4">
                        <input v-model="nickname" placeholder="닉네임" type="nickname" id="nickname" class="form-control form-control-lg" />
                      </div>
                      <form @submit.prevent="signUp">
                      <button class="btn btn-light btn-lg px-5" type="submit">회원가입</button>
                    </form>
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
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      email: null,
      nickname: null,

    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
      const nickname = this.nickname

      const payload = {
        username,
        password1,
        password2,
        email,
        nickname,
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style scoped>
.signup-section {
  width: 100%;
  height: 100%;
}
</style>