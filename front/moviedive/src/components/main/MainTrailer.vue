<template>
  <div class="trailer_box">
    <video
      id="MainTrailer"
      src="https://moviedive.s3.ap-northeast-2.amazonaws.com/trailers/lifeofpi.mp4"
      autoplay="true" 
    >
    </video>
    <div class="info meta-layer">
      <div class="logo-and-text meta-layer">
        <h1>라이프 오브 파이</h1>
      </div>
      <div class="info-wrapper" style="transform: translate3d(0px, 0px, 0px); transition-duration: 1300ms; transition-delay: 0ms; opacity: 1;"><div class="info-wrapper-fade" style="opacity: 1; transition-duration: 600ms; transition-delay: 200ms;">
        <div>
          인도에서 동물원을 운영하던 ‘파이’의 가족은 동물들을 싣고 이민을 떠나는 도중 거센 폭풍우를 만나고 배는 침몰한다. 혼자 살아남은 파이는 가까스로 구명보트에 올라 타지만 다친 얼룩말과 굶주린 하이에나, 그리고 오랑우탄과 함께 표류하게 된다.
        </div>
        <button class="color-secondary hasLabel hasIcon ltr-1jtux27" data-uia="billboard-more-info" type="button"><div class="ltr-1ol9m1e"><div class="medium ltr-1evcx25" role="presentation"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="Hawkins-Icon Hawkins-Icon-Standard"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3ZM1 12C1 5.92487 5.92487 1 12 1C18.0751 1 23 5.92487 23 12C23 18.0751 18.0751 23 12 23C5.92487 23 1 18.0751 1 12ZM13 10V18H11V10H13ZM12 8.5C12.8284 8.5 13.5 7.82843 13.5 7C13.5 6.17157 12.8284 5.5 12 5.5C11.1716 5.5 10.5 6.17157 10.5 7C10.5 7.82843 11.1716 8.5 12 8.5Z" fill="currentColor"></path></svg></div></div><div class="ltr-14rufaj" style="width:1rem"></div><span class="ltr-j0gpa2">상세 정보</span></button></div>
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

<style>
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
  height: 500px;
  overflow: hidden;
  margin: 0px auto;
  position: relative;
}

.info {
    bottom: 30%;
    display: flex;
    flex-direction: column;
    justify-content: end;
    left: 4%;
    position: absolute;
    top: 0;
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