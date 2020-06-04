<template lang="html">
    <v-container>
        <v-layout row>
            <v-flex sm2 md2 lg2>
                <v-spacer></v-spacer>
            </v-flex>
            <v-flex sm8 md8 lg8>
                <v-card tile>
                    <v-card-title class="justify-center">
                        <v-sheet
                          :color="`grey ${theme.isDark ? 'darken-2' : 'lighten-4'}`"
                        >
                          <v-skeleton-loader
                            type="image"
                          >
                              <v-img
                                      src="https://source.unsplash.com/1600x900/?nature,sunrise"
                                      height="320"
                              >
                              </v-img>
                          </v-skeleton-loader>
                        </v-sheet>

                    </v-card-title>
                    <v-card-title class="justify-center">Edit Profile
                        <v-icon>
                            mdi-account
                        </v-icon>
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        <v-form>
                            <v-row>
                                <v-col>
                                    <v-text-field
                                            v-model="user.uname"
                                            label="Username"
                                    >
                                    </v-text-field>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-text-field
                                            v-model="user.fname"
                                            label="First Name"
                                    >
                                    </v-text-field>
                                </v-col>
                                <v-col>
                                    <v-text-field
                                            v-model="user.surname"
                                            label="Surname"
                                            v-on:keyup.enter.native="showPassword"
                                    >
                                    </v-text-field>
                                </v-col>
                                <v-col>
                                    <validation-provider rules="required" v-slot="{ errors }">
                                        <v-text-field
                                                v-model="user.email"
                                                label="Email.."
                                                v-on:keyup.enter.native="showPassword"
                                                append-icon="mdi-email"
                                        >
                                        </v-text-field>
                                        <span>{{ errors[0] }}</span>
                                    </validation-provider>
                                </v-col>
                            </v-row>
                            <validation-provider rules="required" v-slot="{ errors }">
                                <v-text-field
                                        v-model="user.phone"
                                        label="Telephone.."
                                        append-icon="mdi-cellphone"
                                        type="number"
                                        @keyup.enter="handleSubmit()"
                                >
                                </v-text-field>
                                <span>{{ errors[0] }}</span>
                            </validation-provider>

                            <v-btn
                                    @click="handleSubmit"
                                    block
                                    color="primary"
                                    :loading="loading"
                                    :disabled="false"
                                    isActive

                            >Update
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
    import {extend} from 'vee-validate';
    import {required} from 'vee-validate/dist/rules';
    import {ValidationProvider} from 'vee-validate';

    extend('required', {
        ...required,
        message: 'This field is required'
    });
    export default {
        name: 'EditProfileForm',
        inject: ['theme'],
        components: {
            ValidationProvider
        },
        data() {
            return {
            }
        },
        watch: {
            loader() {
                const l = this.loader;
                this[l] = !this[l];

                setTimeout(() => (this[l] = false), 3000);

                this.loader = null
            },
        },
        methods: {
            handleSubmit() {
                this.loader = 'loading'
                //console.log(this.email,this.password);
                let data = {
                    uname: this.user.uname,
                    fname: this.user.fname,
                    surname : this.user.surname ,
                    email: this.user.email,
                    phone : this.user.phone,
                };
                this.$store.dispatch("updateUser", data);
                this.$router.push('/sentemail')

            },
        } ,
        computed : {
            user() {
                return this.$store.state.user ;
            }
        }
    }
</script>

<style lang="css" scoped>
</style>
