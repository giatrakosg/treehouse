<template lang="html">
    <v-container >
    <v-layout row>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm8 md8 lg8>
        <v-card tile>
          <v-card-title class="justify-center">
            <v-img
              src="../../assets/register-image.jpg"
              height="320"
              >
              <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@alxndr_london?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Alexander London"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Alexander London</span></a>
            </v-img>
          </v-card-title >
          <v-card-title class="justify-center">Register
            <v-icon>
              mdi-account
            </v-icon>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-form >
              <v-row>
                <v-col>
                    <v-text-field

                      v-model="username"
                      label="Name"
                      v-on:keyup.enter.native="showPassword"

                    >
                    </v-text-field>
                </v-col>
                <v-col>
                    <v-text-field
                      v-model="surname"
                      label="Surname"
                      v-on:keyup.enter.native="showPassword"
                    >
                    </v-text-field>
                </v-col>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="email"
                      label="Email.."
                      v-on:keyup.enter.native="showPassword"
                      append-icon="mdi-email"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="password"
                      label="Password"
                      append-icon="mdi-eye-off"
                      type="password"
                      @keyup.enter="handleSubmit()"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="passwordRetype"
                      label="Retype Password.."
                      append-icon="mdi-eye-off"
                      type="password"
                      @keyup.enter="handleSubmit()"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
              </v-row>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field
                  v-model="tel"
                  label="Telephone.."
                  append-icon="mdi-cellphone"
                  type="number"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field
                  v-model="address"
                  label="Address"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field
                  v-model="AMKA_id"
                  label="AMKA"
                  type="number"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <v-btn
                @click="loader = 'loading'"
                block
                color="primary"
                :loading="loading"
                :disabled="false"
                isActive

                >Register
              </v-btn>

            </v-form>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
    </v-container>
</template>

<script>
import { extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';
import { ValidationProvider } from 'vee-validate';

extend('required', {
  ...required,
  message: 'This field is required'
});
export default {
  name : 'RegisterForm' ,
  components : {
    ValidationProvider
  },
  data () {
    return {
      email : '' ,
      password : '' ,
      passwordRetype : '',
      tel : '',
      username : '' ,
      surname : '',
      address: '',
      AMKA_id: '' ,
      loader : null ,
      loading  : false
    }
  } ,
  watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]

        setTimeout(() => (this[l] = false), 3000)

        this.loader = null
      },
  },
  methods : {
    handleSubmit() {
      this.loader = 'loading'
        /*
      console.log(this.email,this.password);
      let data = {
        name: this.username,
        first_name: this.username,
        last_name : this.surname ,
        email: this.email,
        password: this.password,
        phone : this.tel,
        address: this.address,
        AMKA_id: this.AMKA_id
      };
      this.$store.dispatch("register", data);
      this.$router.push('/sentemail')
      */
    } ,
  }
}
</script>

<style lang="css" scoped>
</style>
