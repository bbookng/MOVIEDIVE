<template>
  <div class="trailer_box">
    <video
      id="MainTrailer"
      src="https://moviedive.s3.ap-northeast-2.amazonaws.com/trailers/lifeofpi.mp4"
      autoplay="true" 
    >
    </video>
    <div class="info meta-layer" style="width:30rem;">
      <div class="logo-and-text meta-layer" style="text-align:left;">
        <h1 style="font-weight:500">라이프 오브 파이</h1>
        <p>
          인도에서 동물원을 운영하던 ‘파이’의 가족은 동물들을 싣고 이민을 떠나는 도중 거센 폭풍우를 만나고 배는 침몰한다. 혼자 살아남은 파이는 가까스로 구명보트에 올라 타지만 다친 얼룩말과 굶주린 하이에나, 그리고 오랑우탄과 함께 표류하게 된다.
        </p>
        <button type="button" class="btn btn-outline-light" style="width:6rem">상세 정보</button>
      </div>
    </div>
    <NewMovieList/>
  </div>
</template>

<script>
import NewMovieList from '@/components/main/NewMovieList.vue'

export default {
    name: 'MainTrailer',
    components:{
        NewMovieList,
    }
}
</script>

<style scoped>
#MainTrailer {
  bottom: 0;
  left: 0;
  width: 100%;
  right: 0;
  top: 0;
  z-index: 1;
}

.trailer-box {
  display: flex;
  justify-content: center;
  width: 100%;
  margin: 0px auto;
  position: relative;
}

.info {
    bottom: 30%;
    display: flex;
    flex-direction: column;
    left: 4%;
    position: absolute;
    top: 10;
    width: 36%;
    z-index: 10;
    color: white;
}

.trailer-desc h2 p {
  text-align: left;
  color: white;
  z-index: 10;
}

.billboard-row .billboard .info .logo-and-text {
    transition: transform 1.5s cubic-bezier(.165,.84,.44,1);
    width: 100%;
}
</style>