<template>
  <div
    class="modal fade"
    id="movieDetail"
    tabindex="-1"
    aria-labelledby="movieDetail"
    aria-hidden="true"
  >
    <div v-if="movie">
      <div class="modal-dialog">
        <div class="modal-content">
          <div
            class="
              modal-header
              d-flex
              flex-column
              justify-content-end
              align-items-start
            "
            :style="`background-image: url(${poster}); background-size: cover; position:relative;`"
          >
            <button
              id="movie-detail-quit"
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
            <div style="padding: 20px">
              <div class="d-flex" style="background-color: transparent; border:none;">
                <p
                  id="movie-detail-title"
                  style="color: white; font-size: 50px; margin: 0"
                >
                  {{ movie.title }}
                </p>
                <button @click="likeMovie"
                style="border: none; background-color: transparent;
                padding:0">
                  <img
                    src="https://moviedive.s3.ap-northeast-2.amazonaws.com/like.png"
                    style="border: none; background-color: transparent; color:white width:30px; height:30px; padding:0"
                    alt=""
                  />
                </button>
              </div>
              <div class="d-flex" style="color: white">
                <p>★ {{ movie.vote_average }}</p>
                <span style="margin-left: 12px"> 12세, 1시간 45분</span>
              </div>
            </div>
            <div id="streaming-button-container">
              <button
                class="streaming-button"
                id="netflix-icon"
                style="
                  padding: 0;
                  overflow: hidden;
                  border: none;
                  position: relative;
                "
              >
                <img
                  src="https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fwp-content%2Fblogs.dir%2F11%2Ffiles%2F2019%2F02%2Fnetflix-introduction-logo-nouveau-1.jpg?q=90&w=1400&cbr=1&fit=max"
                  style="
                    height: 60px;
                    width: 90px;
                    padding: 0;
                    border: none;
                    position: absolute;
                    left: -15px;
                    top: 0;
                  "
                  alt=""
                />
              </button>
              <button
                class="streaming-button"
                id="watcha-icon"
                style="
                  padding: 0;
                  overflow: hidden;
                  border: none;
                  margin-left: 2px;
                  margin-right: 2px;
                  position: relative;
                  background-color: black;
                "
              >
                <img
                  src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjEwMDJfMTI0%2FMDAxNjY0Njg1MTQxMDU4.6Ej0tgt-9FU9kHYVEGjmpDGDfua0-g8seFnSaS5DhEgg.awWscBxkfp_V4KWQadiHh0kNw8zrXQJjfHgIC31mGhUg.PNG.ews1016%2Funnamed.png&type=sc960_832"
                  style="
                    height: 50px;
                    width: 50px;
                    padding: 0;
                    border: none;
                    position: absolute;
                    left: 5px;
                    top: 5px;
                  "
                  alt=""
                />
              </button>
              <button
                class="streaming-button"
                id="wavve-icon"
                style="
                  padding: 0;
                  overflow: hidden;
                  border: none;
                  position: relative;
                  background-color: black;
                "
              >
                <img
                  src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/7a18af97be14824f6b57"
                  style="
                    height: 60px;
                    width: 60px;
                    padding: 0;
                    border: none;
                    position: absolute;
                    left: 0px;
                    top: 0px;
                  "
                  alt=""
                />
              </button>
            </div>
          </div>
          <div class="modal-body">
            <p>{{ movie.overview }}</p>
          </div>
          <div>
            <button
              id="movie-detail-create-review"
              data-bs-dismiss="modal"
              @click="goToWriteReview"
            >
              리뷰 작성하기
            </button>
            <hr />
            <div
              style="
                padding-bottom: 20px;
                padding-left: 30px;
                padding-right: 30px;
              "
            >
              <p>최근 리뷰</p>
              <div
                class="movie-detail-review"
                v-for="review in movie.reviews"
                :key="review.id"
                style="margin: 5px"
              >
                <p
                  style="
                    margin: 0;
                    width: 70%;
                    text-align: left;
                    margin-left: 15px;
                  "
                >
                  {{ review.title }}
                </p>

                <p style="margin: 0; width: 15%">
                  {{ review.created_string }}
                </p>
                <div style="width: 15%" class="d-flex align-items-center">
                  <img
                    class="movie-detail-review-user-profile"
                    style="margin-right: 7px"
                    :src="review.user.profile_img"
                    alt="유저 프로필 사진"
                  />
                  <p style="margin: 0">{{ review.user.nickname }}</p>
                </div>
              </div>
              <button
                id="movie-detail-create-review"
                data-bs-dismiss="modal"
                style="margin-top: 8px"
                @click="goToMoreReview"
              >
                리뷰 더보기
              </button>
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
const API_URL = "https://moviedive.co.kr/api";

export default {
  name: "MovieDetail",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["movie", "currentUser"]),
    poster() {
      return "https://image.tmdb.org/t/p/original/" + this.movie.backdrop_path;
    },
  },
  methods: {
    likeMovie() {
      axios({
        url: `${API_URL}/movies/${this.movie.pk}/like/`,
        method: "post",
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then(() => {
        this.getMovieDetail();
      });
    },
    goToWriteReview() {
      return this.$router.push({ name: "create_review" });
    },
    goToMoreReview() {
      return this.$router.push({ name: "community" });
    },
  },
};
</script>

<style scoped>
#movieDetail {
  z-index: 2000;
}
.modal,
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  right: 0;
}
.movie-detail-review {
  display: flex;
  align-items: center;
  border: 1px solid black;
  margin-left: 40px;
  margin-right: 40px;
  height: 35px;
  border-radius: 17.5px;
}
.modal-content {
  width: 700px;
  height: 850px;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.modal-header {
  padding: 0;
  height: 400px;
  position: relative;
}
.movie-detail-poster {
  padding: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  cursor: none;
}

#movie-detail-title {
  color: white;
}
.modal-footer {
  height: 150px;
}
.modal-card {
  position: relative;
  max-width: 80%;
  margin: auto;
  margin-top: 30px;
  padding: 20px;
  background-color: black;
  min-height: 500px;
  opacity: 1;
}
.modal-body {
  padding: 20px;
  padding-top: 50px;
}
#movie-detail-quit {
  position: absolute;
  top: 10px;
  right: 10px;
  color: white;
}
.movie-detail-review-user-profile {
  height: 20px;
  width: 20px;
  border-radius: 50%;
  padding: 0;
}
.streaming-button {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: 1px solid white;
}
#streaming-button-container {
  padding-left: 20px;
  position: absolute;
  top: 370px;
}
#movie-detail-create-review {
  background: transparent;
  border: none;
  text-decoration: underline;
}
</style>