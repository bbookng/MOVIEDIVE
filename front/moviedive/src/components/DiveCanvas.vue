<template>
  <div id="dive-canvas"></div>
</template>

<script>
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { Particles } from '../modules/Particles';

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

      // MOVIEDIVE hemisphere
      // 이미지 로드
      const loader = new THREE.TextureLoader();
      loader.setPath( '/images/' );
      this.texture = new THREE.TextureLoader().load(
        require( "./images/noxm.png" )
      );
      this.texture.generateMipmaps = false;
      const geometry_md = new THREE.SphereGeometry( 0.1, 32, 16, 0, Math.PI, 0, Math.PI  );
      const material_md = new THREE.MeshBasicMaterial( { map: this.texture } )
      
      const moviedive = new THREE.Mesh( geometry_md, material_md );
      moviedive.rotation.x = -0.4
      moviedive.name = 'moviedive'
      scene.add(moviedive);

      this.texture_h = new THREE.TextureLoader().load(
        require( "./images/lb.png" )
      );

      const geometry_h = new THREE.SphereGeometry( 0.1, 32, 16, 0, Math.PI, 0, Math.PI  );
      const material_h = new THREE.MeshBasicMaterial( { map: this.texture_h } )
      
      const hemisphere = new THREE.Mesh( geometry_h, material_h );
      hemisphere.rotation.x = -0.4
      hemisphere.rotation.y = 3.141592
      hemisphere.rotation.z = 0
      hemisphere.name = 'hemisphere'
      scene.add(hemisphere);

      // 구체 전체 배열
      const sphere = [moviedive, hemisphere]

      // Points by class - !! 이미지 문제만 해결하면 됨 !!
      const p1 = new Particles('./images/p01.png', 20)
      scene.add(p1)

      // 그리기
      function draw() {
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

      // 레이캐스터로 클릭 감지
      const mouse = new THREE.Vector2()
      const raycaster = new THREE.Raycaster()

      let flag = false
      function checkClick() {  
        raycaster.setFromCamera(mouse, camera)
        const intersects = raycaster.intersectObjects(sphere)
        for (const item of intersects) {
          if (item.object.name === 'moviedive' || item.object.name === 'hemisphere') {
            flag = true

          }
        }
      }

      // 이벤트
      window.addEventListener('resize', setSize);
      canvas.addEventListener('click', e => {
        mouse.x = e.clientX / canvas.clientWidth * 2 - 1
        mouse.y = -(e.clientY / canvas.clientHeight * 2 -  1)
        checkClick()
        if (flag) {
          this.$emit('logo-clicked')
        }
      })

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