<template>
  <div class="publisher">
    <h1>Ask Smart 😊</h1>
    <div class="md-layout md-gutter">
      <div>
        <md-card class="md-layout-item md-size-100" md-with-hover id="pubCard" >
          <md-card-media-cover>
            <md-card-media >
              <img src="pub.png" alt="Skyscraper">
            </md-card-media>
          </md-card-media-cover>
        </md-card>
      </div>

      <div class="md-layout-item md-size-75">
        <div>
          <form novalidate class="md-layout" @submit.prevent="validateUser">
            <md-card class="md-layout-item md-size-100 md-small-size-100">
              <md-card-header>
                <div class="md-title">Publish New Questions</div>
              </md-card-header>

              <md-card-content>
                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-small-size-100">
                    <md-field>
                      <label for="question">Question</label>
                      <md-input name="question" id="question" v-model="form.question"/>
                    </md-field>
                  </div>
                </div>
                <br>

                <div class="md-layout-item md-small-size-100">
                  <md-field>
                    <label for="voters">Amount of voters</label>
                    <md-input type="number" id="voters" name="voters" v-model="form.voter_size"/>
                  </md-field>
                </div>
                <br>
                <div class="md-layout-item md-small-size-100">
                  <md-field>
                    <label for="init_pool">Initial Pool</label>
                    <md-input type="number" id="init_pool" name="init_pool" v-model="form.initial_pool"/>
                  </md-field>
                </div>                  
                <br>
                <div>
                  <md-field>
                    <label for="audience_labels">Audience Labels</label>
                    <md-select v-model="form.audience_labels" name="audience_labels" id="audience_labels" multiple>
                      <md-option value="Shenzhen">Shenzhen</md-option>
                      <md-option value="Guangzhou">Guangzhou</md-option>
                      <md-option value="Shanghai">Shanghai</md-option>
                      <md-option value="Hongkong">Hongkong</md-option>
                      <md-option value="PaloAlto">Palo Alto</md-option>
                    </md-select>
                  </md-field>                  
                </div>

              </md-card-content>

              <md-card-actions>
                <md-button @click="publish" class="md-primary">Then Publish Your Question like a boss😎</md-button>
              </md-card-actions>
            </md-card>
          </form>
        </div>        
      </div>

  
    </div>
  </div>
  
</template>

<style>
.publisher {
  width: 80%;
  margin: auto;
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
  name: 'FormValidation',
  mixins: [validationMixin],
  data: () => ({
    form: {
      question: null,
      voter_size: null,
      initial_pool: null,
      audience_labels: [],
    }
  }),
  methods: {
    publish: function(){
      console.log(this.form.question)
      console.log(this.form.voter_size)
      console.log(this.form.initial_pool)
      console.log(this.form.audience_labels)
      this.$http.post('http://localhost:8081/beaky/publish',{
        "quesiton": this.form.question,
        "size": this.form.voter_size,
        "initial_pool": this.form.initial_pool,
        "audience_labels": this.form.audience_labels  
      })
      .then((response)=>{
        console.log(response.bodyText);
      })
    }
  }
}
</script>
