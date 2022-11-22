import * as THREE from 'three';

export class Particles {

	constructor(scene, imgUrl, count, size) {
		this.geometry = new THREE.BufferGeometry();
		this.positions = new Float32Array(count * 3);
		for (let i = 0; i < this.positions.length; i++) {
			this.positions[i] = (Math.random() - 0.5) * 10;
		}
		this.geometry.setAttribute(
			'position',
			new THREE.BufferAttribute(this.positions, 3) // 1개의 Vertex(정점)를 위해 값 3개 필요
		);
	
		// 이미지 로드
		this.textureLoader = new THREE.TextureLoader();
		this.particleTexture = this.textureLoader.load(imgUrl);
	
		this.material = new THREE.PointsMaterial({
			size: size,
			map: this.particleTexture,
			// 파티클 이미지를 투명하게 세팅
			transparent: true,
			alphaMap: this.particleTexture,
			depthWrite: false
		});
	
		this.particles = new THREE.Points(this.geometry, this.material);
		scene.add(this.particles)
    // return this.particles;
	}
	
	
}