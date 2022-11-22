import * as THREE from 'three';

export class Poster {
	constructor(info) {
        // 텍스처로 포스터 넣기
        this.texture = new THREE.TextureLoader().load(info.imgUrl);
        this.texture.generateMipmaps = false;
        
        this.poster = new THREE.Mesh(
            new THREE.PlaneGeometry( 4, 4 ),
            new THREE.MeshStandardMaterial({
                map: this.texture,
                transparent: true,
                depthWrite: false
             })
        );
		this.poster.castShadow = true; 
		this.poster.position.set(info.x, 2.5, info.z - 5);
		
        info.scene.add(this.poster);
	}
}