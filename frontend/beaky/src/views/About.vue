<template>
  <div class="about">
    <h1>I think I'm a .....</h1>
    <md-card md-with-hover id="pubCard" >
      <md-card-media-cover>
        <md-card-media >
          <a href="#/publish"><img src="pub.png" alt="Skyscraper"></a>
        </md-card-media>
      </md-card-media-cover>
    </md-card>

    <md-card md-with-hover>
      <md-card-media-cover>
        <md-card-media >
          <a href="#/voter"><img src="voter.png" alt="Skyscraper"></a>
        </md-card-media>
      </md-card-media-cover>
    </md-card>

    <md-card md-with-hover>
      <md-card-media-cover>
        <md-card-media >
          <a href="#/subscriber"><img src="sub.png" alt="Skyscraper"></a>
        </md-card-media>
      </md-card-media-cover>
    </md-card>  
    <div>
      <br>
      <br>
      <br>
    </div>
    <br>
    
  </div>
</template>


<style>
.about {
  width: 80%;
  margin: auto;
}

.md-card {
  width: 22%;
  margin: 2%;
  display: inline-block;
  vertical-align: top;
}

.initButton{
  width: 25%;
  margin: 10%;
  display: inline-block;
  vertical-align: top;
}
</style>

<script>
export default {
  name: 'About',
  methods: {
    btn_click: () => {
      alert('clicked')
    },
    jump_to_pub: () => {
      window.location.assign('#/publish');
    },
    jump_to_vote: () => {
      window.location.assign('#/voter');
    },
    jump_to_sub: () => {
      window.location.assign('#/subscriber');
    }
  }
};
</script>