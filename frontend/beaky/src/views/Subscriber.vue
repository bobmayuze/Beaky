<template>
  <div class="subscriber">
    <h1>Search For What You Need 😋</h1>
    <div class="md-layout md-gutter">
      <div>
        <md-card class="md-layout-item md-size-100" md-with-hover id="subCard" >
          <md-card-media-cover>
            <md-card-media >
              <img src="sub.png" alt="Skyscraper">
            </md-card-media>
          </md-card-media-cover>
        </md-card>
      </div>

      <div class="md-layout-item md-size-75">
        <md-field md-inline>
          <md-icon>search</md-icon>
          <label>Let's see if we can find something here😏</label>
          <md-input @keyup="foo" v-model="query"></md-input>

        </md-field>
        <!-- {{related_list }} -->
        <!-- <h1 v-for="q in question_list">{{q}}</h1> -->
        <md-card md-with-hover v-for="q in related_list">
            <md-card-header>
              <div class="md-title">{{q.question}}</div>
              <div class="md-subhead">{{q._id}}</div>
            </md-card-header>

            <md-card-content>
              Price: $ {{ 0.2 * q.initial_pool }}
              <br>
              Labels: {{ q.audience_labels}}
            </md-card-content>

            <md-card-actions>
              <md-button class="md-raised md-accent" @click="show = true">Purchase 💵 </md-button>
            </md-card-actions>
        </md-card>

        <md-card md-with-hover>
            <md-card-header>
              <div class="md-title">Should I put salt in my coffie</div>
              <div class="md-subhead">5b2f14b7420b2c0008c58d1d</div>
            </md-card-header>

            <md-card-content>
              Price: $ 12
              <br>
              Labels: ["Shanghai"]
            </md-card-content>

            <md-card-actions>
              <md-button class="md-raised md-accent" @click="show = true">Purchase 💵 </md-button>
            </md-card-actions>
        </md-card>

        <md-dialog-alert
          :md-active.sync="show"
          md-title="YES, DEFINITELY😎"
          md-content="The majority thinks this is a solid move." />

      </div>

  
    </div>
  </div>
  
</template>

<style scoped>
.subscriber {
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

export default {
  name: 'subscriber',
  data: () => ({
    show: false,
    query: null,
    question_list: null,
    related_list: null,
  }),
  methods: {
    foo: function () {
      let query_set = this.query.split(' ')
      this.related_list = []
      for (let index = 0; index < this.question_list.length; index++) {
        const question = this.question_list[index];
        // console.log(question.audience_labels);
        let difference = query_set.filter(x => !question.audience_labels.includes(x));
        if (difference.length == 0) {
          this.related_list.push(question)
        }
      }
      console.log("Now we have",this.related_list);
    }
    
  },
  created: function () {
      this.$http.get('http://localhost:8081/beaky/getAllClosedQuestions')
    .then((response)=>{
      console.log(response.body.length);
      this.question_list = response.body;
    })
  }
}
</script>
