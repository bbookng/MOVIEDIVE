import * as THREE from 'three';

export default function dive(data) {
	//moviedive
	const loader = new THREE.TextureLoader();
	loader.setPath( '/images/' );
	const texture = loader.load('noxm.png');
	texture.generateMipmaps = false;
    texture.minFilter = THREE.LinearFilter;

	const geometry_md = new THREE.SphereGeometry( 0.1, 32, 16, 0, Math.PI, 0, Math.PI  );
	const material_md = new THREE.MeshBasicMaterial( { map: texture } )
	
	const moviedive = new THREE.Mesh( geometry_md, material_md );
	moviedive.rotation.x = -0.4

	data.scene.add(moviedive);

	// hemisphere
	const loader_h = new THREE.TextureLoader();
	loader_h.setPath( '/images/' );
	const texture_h = loader.load('lb.png');
	texture.generateMipmaps = false;
    texture.minFilter = THREE.LinearFilter;

	const geometry_h = new THREE.SphereGeometry( 0.1, 32, 16, 0, Math.PI, 0, Math.PI  );
	const material_h = new THREE.MeshBasicMaterial( { map: texture_h } )
	
	const hemisphere = new THREE.Mesh( geometry_h, material_h );
	hemisphere.rotation.x = -0.4
	hemisphere.rotation.y = 3.141592
	hemisphere.rotation.z = 0
	d.scene.add(hemisphere);

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
	const textureLoader = new THREE.TextureLoader();
	const particleTexture = textureLoader.load('/images/glow1.png');

	const material = new THREE.PointsMaterial({
		size: 0.7,
		map: particleTexture,
		// 파티클 이미지를 투명하게 세팅
		transparent: true,
		alphaMap: particleTexture,
		depthWrite: false
	});

	const particles = new THREE.Points(geometry, material);
	this.scene.add(particles);
}

