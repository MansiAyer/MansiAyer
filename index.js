module.exports = async (req, res) => {

    renderJoke = `<svg width="500" fill="none" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
				.main {
			text-align: center;
			background: linear-gradient(#000000,#252942);
		}
		.jok {
			box-shadow: 0 0 1px 1px #82C1FF,  /* inner white */
        0 0 8px 10px #030457;
			border: 1px solid #091980;
			border-radius: 12px;
			margin: 10px;
		}
		.stt {

		}
			</style>
			<div class="main">
	
	<img src="https://vignette.wikia.nocookie.net/leagueoflegends/images/6/68/KDA_Logo_1.png/revision/latest?cb=20181104035006"/>

	<div align="center"><span>  
  <img width="150px" height="150px" src="https://vignette.wikia.nocookie.net/leagueoflegends/images/3/30/KDA_Orb.gif/revision/latest/top-crop/width/220/height/220?cb=20181208112614"></img> 
  <img class="jok" src="https://readme-jokes.vercel.app/api?bgColor=%23000000&aColor=%2382C1FF&qColor=%23606FFC&textColor=%232289F0&borderColor=%23000000"> </img>
  <img width="150px" height="150px" src="https://vignette.wikia.nocookie.net/leagueoflegends/images/3/30/KDA_Orb.gif/revision/latest/top-crop/width/220/height/220?cb=20181208112614"></img> 
  </span></div>

	<img src="https://preview.redd.it/rxes6762mzj51.png?auto=webp&s=203712b3b3dfd66aad6785d7b3ec005e71cb400a"/>

	<div align="center"><img class="stt" src="https://github-readme-stats.vercel.app/api?username=MansiAyer&theme=tokyonight"> </img></div>

	<img src="https://preview.redd.it/ltmsdft4efk51.png?width=3840&format=png&auto=webp&s=edf1489dac6bfd5a9b5f70e03fb6c6c840d01fbb"/>
</div>

		</div>
	</foreignObject>
</svg>`;
    // Sets the type of content sent
  res.setHeader('Content-Type', 'image/svg+xml');
  // Set the Cache type to public (Any cache can store the data) and the max-age
  res.setHeader('Cache-Control', `public, max-age=${cacheSeconds}`);
  res.send(renderJoke);
};
