<template>
  <div id="dive-canvas">
  </div>
</template>

<script>
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';


export default {
  name: 'DiveCanvas',
  data() {
    return {
        scene: new THREE.Scene(),
        camera: null,
        renderer: THREE.WebGLRenderer,
        mesh: new THREE.Mesh,
        controls: null,
        canvas: null,
        isLanding: true,
        texture: null,
        texture_h: null,
        particleTexture: null,
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      // Renderer
      const canvas = document.querySelector('#dive-canvas');
      const renderer = new THREE.WebGLRenderer({
        // canvas,
        antialias: true
      });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(window.devicePixelRatio > 1 ? 2 : 1);
      renderer.setClearColor('#000911');
      canvas.appendChild(renderer.domElement)

      // Scene
      const scene = new THREE.Scene();

      // Camera
      const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
      );
      camera.position.y = 1.5;
      camera.position.z = 4;
      scene.add(camera);

      // Light
      const ambientLight = new THREE.AmbientLight('white', 0.5);
      scene.add(ambientLight);

      const directionalLight = new THREE.DirectionalLight('white', 1);
      directionalLight.position.x = 1;
      directionalLight.position.z = 2;
      scene.add(directionalLight);

      // Controls
      const controls = new OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      
      // AxesHelper
      // const axesHelper = new THREE.AxesHelper();
      // scene.add(axesHelper)

      // MOVIEDIVE hemisphere
      // 이미지 로드
      // const loader = new THREE.TextureLoader();
      // loader.setPath( '/images/' );
      this.texture = new THREE.TextureLoader().load(
        require( "./images/noxm.png" )
      );
      // const texture = loader.load('https://moviedive.s3.ap-northeast-2.amazonaws.com/noxm.png');
      // texture.generateMipmaps = false;
      // texture.minFilter = THREE.LinearFilter;
      const geometry_md = new THREE.PlaneGeometry( 0.2, 0.2 )
      // const geometry_md = new THREE.SphereGeometry( 0.1, 32, 16, 0, Math.PI, 0, Math.PI  );
      const material_md = new THREE.MeshBasicMaterial( { map: this.texture } )
      
      const moviedive = new THREE.Mesh( geometry_md, material_md );
      moviedive.rotation.x = -0.4

      scene.add( moviedive );

      // hemisphere
      // loader_h.setPath( '/images/' );
      // const texture_h = new THREE.TextureLoader().load('./images/lb.png');
      this.texture_h = new THREE.TextureLoader().load(
        require( "./images/lb.png" )
      );
      // texture.generateMipmaps = false;
      // texture.minFilter = THREE.LinearFilter;

      const geometry_h = new THREE.SphereGeometry( 0.1, 32, 16, 0, Math.PI, 0, Math.PI  );
      const material_h = new THREE.MeshBasicMaterial( { map: this.texture_h } )
      
      const hemisphere = new THREE.Mesh( geometry_h, material_h );
      hemisphere.rotation.x = -0.4
      hemisphere.rotation.y = 3.141592
      hemisphere.rotation.z = 0
      scene.add( hemisphere );

      // Points
      const geometry = new THREE.BufferGeometry();
      const count = 800;
      const positions = new Float32Array(count * 3);
      for (let i = 0; i < positions.length; i++) {
        positions[i] = (Math.random() - 0.5) * 10;
      }
      geometry.setAttribute(
        'position',
        new THREE.BufferAttribute(positions, 3) // 1개의 Vertex(정점)를 위해 값 3개 필요
      );

      // 이미지 로드
      // const textureLoader = new THREE.TextureLoader();
      // const particleTexture = textureLoader.load('./images/glow1.png');
      this.particleTexture = new THREE.TextureLoader().load(
        require( "./images/glow1.png" )
      );

      const material = new THREE.PointsMaterial({
        size: 0.7,
        map: this.particleTexture,
        // 파티클 이미지를 투명하게 세팅
        transparent: true,
        alphaMap: this.particleTexture,
        depthWrite: false
      });

      const particles = new THREE.Points(geometry, material);
      scene.add( particles );

      // 그리기
      // const clock = new THREE.Clock();

      function draw() {
        // const delta = clock.getDelta();

        controls.update();

        renderer.render(scene, camera);
        renderer.setAnimationLoop(draw);
      }

      function setSize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.render(scene, camera);
      }

      // 이벤트
      window.addEventListener('resize', setSize);

      draw();
		}
  }
}
</script>

<style>
  #dive-canvas {
    position: absolute;
    left: 0;
    top: 0;
    margin: 0;
  }
</style>