<template>
  <div class="voter">
    <h1>Think Carefully 🤔</h1>
    <div class="md-layout md-gutter">
      <div>
        <md-card class="md-layout-item md-size-100" md-with-hover id="pubCard" >
          <md-card-media-cover>
            <md-card-media >
              <img src="voter.png" alt="Skyscraper">
            </md-card-media>
          </md-card-media-cover>
        </md-card>
      </div>

      <div class="md-layout-item md-size-75">
        <div>
          <form novalidate class="md-layout" @submit.prevent="validateUser">
            <md-card class="md-layout-item md-size-100 md-small-size-100">
              <md-card-header>

                <br>
                <h1>{{ current_question.question_context }}</h1>
                {{ current_question.quesiton_id}}
                <br>
                <br>
              </md-card-header>

              <md-card-content>
                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-size-20">
                    <h2>Voting fee</h2>
                  </div>
                  <div class="md-layout-item md-size-80">
                    <h1>$ 80</h1>
                  </div>
                </div>
                <br>

                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-size-20">
                    <h2>Current Pool Size</h2>
                  </div>
                  <div class="md-layout-item md-size-80">
                    <h1>$ 1880</h1>
                  </div>
                </div>
                <br>

                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-size-20">
                    <h2>Labels</h2>
                  </div>
                  <div class="md-layout-item md-size-80">
                    <h1>Shanghai, Beijing</h1>
                  </div>
                </div>
                <br>                

              </md-card-content>

            </md-card>
          </form>

          <md-button  @click="upVote" class="md-fab">
            <md-icon>thumb_up</md-icon>
          </md-button>

          <md-button @click="downVote" class="md-fab">
            <md-icon>thumb_down</md-icon>
          </md-button>

          <md-button @click="pass" class="md-fab">
            <md-icon>navigate_next</md-icon>
          </md-button>
        </div>        
      </div>

  
    </div>
  </div>
  
</template>

<style scoped>
.voter {
  width: 80%;
  margin: auto;
}
.md-button.md-fab.mybtnstyle {
   background-color: blue;
}

.md-button {
  padding: 1%;
  margin: 5%;
}
</style>


<script>

import { validationMixin } from 'vuelidate'
import {
  required,
  email,
  minLength,
  maxLength
} from 'vuelidate/lib/validators'

function arr_diff (a1, a2) {

    var a = [], diff = [];

    for (var i = 0; i < a1.length; i++) {
        a[a1[i]] = true;
    }

    for (var i = 0; i < a2.length; i++) {
        if (a[a2[i]]) {
            delete a[a2[i]];
        } else {
            a[a2[i]] = true;
        }
    }

    for (var k in a) {
        diff.push(k);
    }

    return diff;
}

export default {
  name: 'voter',
  data: () => ({
    current_question: {
      question_context: null,
      quesiton_id: null,
      voting_fee : null,
      pool_size : null,
      question_labels: null,
      choice: null,

    },
    form: {
      question: null,
      voter_size: null,
      initial_pool: null,
      audience_labels: [],
    }
  }),
  methods: {
    upVote: function(){
      this.$http.post('http://localhost:8081/beaky/vote',{
        "question_id": this.current_question.quesiton_id,
        "choice": "yes",
      })
      .then((response)=>{
        sessionStorage.setItem(this.current_question.quesiton_id, this.current_question.quesiton_id);
        alert("Voted successfully!🤑🤑🤑")
        window.location.reload(false);
      })      
    },
    downVote: function(){
      this.$http.post('http://localhost:8081/beaky/vote',{
        "question_id": this.current_question.quesiton_id,
        "choice": "no",
      })
      .then((response)=>{
        sessionStorage.setItem(this.current_question.quesiton_id, this.current_question.quesiton_id);
        alert("Voted successfully!🤑🤑🤑")
        window.location.reload(false); 
      })
    },
    pass: function(){
      sessionStorage.setItem(this.current_question.quesiton_id, this.current_question.quesiton_id);
      window.location.reload(false); 

    },      
  },
  created: function () {
    this.$http.get('http://localhost:8081/beaky/getIds')
    .then((response)=>{
      
      let id_list = response.body;
      console.log();
      let voted_list = Object.keys(sessionStorage);
      let difference = id_list.filter(x => !voted_list.includes(x));
      console.log("DIFF: ",difference);
      this.$http.post('http://localhost:8081/beaky/getQuestionById',{"question_id":difference[0]}).then((response)=>{
        console.log(response.body);
        let question = response.body;
        this.current_question.question_context = question.question
        this.current_question.quesiton_id = question._id
        
      })
    })
  }
}
</script>
