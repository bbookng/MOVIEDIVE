<template>
    <div>
      <div id="three-canvas"></div>
      <div class="sections">
        <section class="section">
          <h2>01</h2>
          <h3>{{ recommend_movies[0].title }}</h3>
        </section>
        <section class="section">
          <h2>02</h2>
          <h3>{{ recommend_movies[1].title }}</h3>
        </section>
        <section class="section">
          <h2>03</h2>
          <h3>{{ recommend_movies[2].title }}</h3>
        </section>
        <section class="section">
          <h2>04</h2>
          <h3>{{ recommend_movies[3].title }}</h3>
        </section>
        <section class="section">
          <h2>05</h2>
          <h3>{{ recommend_movies[4].title }}</h3>
        </section>
        <section class="section">
          <h2>06</h2>
          <h3>{{ recommend_movies[5].title }}</h3>
        </section>
        <section class="section">
          <h2>07</h2>
          <h3>{{ recommend_movies[6].title }}</h3>
        </section>
        <section class="section">
          <h2>08</h2>
          <h3>{{ recommend_movies[7].title }}</h3>
        </section>
        <section class="section">
          <h2>09</h2>
          <h3>{{ recommend_movies[8].title }}</h3>
        </section>
        <section class="section">
          <h2>10</h2>
          <h3>{{ recommend_movies[9].title }}</h3>
        </section>
      </div>
    </div>
</template>

<script>
import * as THREE from 'three';
import { Poster } from '../modules/Poster';
import gsap from 'gsap';
import axios from 'axios';
import lodash from 'lodash';

const API_URL = 'https://moviedive.co.kr/api'


export default {
  name: 'DeepDiveView',
  data() {
    return {
      recommend_movies: null,
    }
  },
  created() {
    this.getRecommends()
  },
  methods: {
    getRecommends() {
      axios({
        url: `${API_URL}/movies/recommend/`,
        method: 'get',
        headers: this.$store.getters.authHeader,
      })
      .then((res) => {
        this.recommend_movies = lodash.sampleSize(res.data, 10)
      })
      .then(() => {
        this.init()
      })
    },

    init() {
      const canvas = document.querySelector('#three-canvas');
      const renderer = new THREE.WebGLRenderer({
        antialias: true
      });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(window.devicePixelRatio > 1 ? 2 : 1);
      renderer.shadowMap.enabled = true;
      renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      canvas.appendChild(renderer.domElement)

      // Scene
      const scene = new THREE.Scene();
      scene.background = new THREE.Color('white');

      // Camera
      const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
      );
      camera.position.set(-5, 2, 25);
      scene.add(camera);

      // Light
      const ambientLight = new THREE.AmbientLight('white', 0.5);
      scene.add(ambientLight);

      const spotLight = new THREE.SpotLight('white', 0.7);
      spotLight.position.set(0, 150, 100);
      spotLight.castShadow = true;
      spotLight.shadow.mapSize.width = 2048;
      spotLight.shadow.mapSize.height = 2048;
      spotLight.shadow.camera.near = 1;
      spotLight.shadow.camera.far = 200;
      scene.add(spotLight);

      // Mesh
      const floorMesh = new THREE.Mesh(
        new THREE.PlaneGeometry(100, 100),
        new THREE.MeshStandardMaterial({ color: 'white' })
      );
      floorMesh.rotation.x = -Math.PI / 2;
      floorMesh.receiveShadow = true;
      scene.add(floorMesh);
     
      const posters = [];
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[0].poster_path}`, x: -5, z: 20 }));
      console.log(posters)
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[1].poster_path}`, x: 7, z: 10 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[2].poster_path}`, x: -10, z: 0 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[3].poster_path}`, x: 10, z: -10 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[4].poster_path}`, x: -5, z: -20 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[5].poster_path}`, x: -5, z: -30 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[6].poster_path}`, x: 7, z: -40 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[7].poster_path}`, x: -10, z: -50 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[8].poster_path}`, x: 10, z: -60 }));
      posters.push(new Poster({ scene, imgUrl: `https://image.tmdb.org/t/p/original/${this.recommend_movies[9].poster_path}`, x: -5, z: -70 }));




      // 그리기
      function draw() {
        renderer.render(scene, camera);
        renderer.setAnimationLoop(draw);
      }
      
      let currentSection = 0;
      function setSection() {   
        const newSection = Math.round(window.scrollY / window.innerHeight);


        if (currentSection !== newSection) {
          gsap.to(
            camera.position,
            {
              duration: 1,
              x: posters[newSection].poster.position.x,
              z: posters[newSection].poster.position.z + 5,
            }
          );
          currentSection = newSection;
        }
      }

      function setSize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.render(scene, camera);
      }

      // 이벤트
      window.addEventListener('scroll', setSection);
      window.addEventListener('resize', setSize);

      draw();
    }
  },
}
</script>

<style scoped>
body {
	margin: 0;
}
#three-canvas {
	position: fixed;
	left: 0;
	top: 10;
}
.sections {
	position: relative;
	z-index: 1;
}
.section {
	box-sizing: border-box;
	padding: 5rem;
	height: 100vh;
}
.section h2 {
	margin: 0;
	font-size: 10vmin;
}
.section:nth-child(odd) {
	text-align: right;
}
</style>