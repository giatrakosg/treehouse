<template lang="html">
    <v-container>
        <v-card tile>
            <v-card-title class="justify-center">
                <v-img
                        src="../../assets/register-image.jpg"
                        height="320"
                >
                    <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px"
                       href="https://unsplash.com/@alxndr_london?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge"
                       target="_blank" rel="noopener noreferrer"
                       title="Download free do whatever you want high-resolution photos from Alexander London"><span
                            style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg"
                                                                              style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white"
                                                                              viewBox="0 0 32 32"><title>unsplash-logo</title><path
                            d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span
                            style="display:inline-block;padding:2px 3px">Alexander London</span></a>
                </v-img>
            </v-card-title>
            <v-card-title class="justify-center">Login
                <v-icon>
                    mdi-account
                </v-icon>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
                <v-form>
                    <v-row>
                        <v-col>
                            <validation-provider rules="required" v-slot="{ errors }">
                                <v-text-field
                                        v-model="uname"
                                        label="Username.."
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
                                        label="Password.."
                                        append-icon="mdi-eye-off"
                                        type="password"
                                        @keyup.enter="handleSubmit()"
                                >
                                </v-text-field>
                                <span>{{ errors[0] }}</span>
                            </validation-provider>
                        </v-col>
                    </v-row>
                    <v-btn
                            @click="handleSubmit"
                            block
                            color="primary"
                            :loading="loading"
                            :disabled="false"
                            isActive

                    >Login
                    </v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
    import {extend} from 'vee-validate';
    import {required} from 'vee-validate/dist/rules';
    import {ValidationProvider} from 'vee-validate';
    import router from "../../router";

    extend('required', {
        ...required,
        message: 'This field is required'
    });
    export default {
        name: 'LoginForm',
        components: {
            ValidationProvider
        },
        data() {
            return {
                password: '',
                uname : ''
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
            async handleSubmit() {
                this.loader = 'loading'
                console.log(this.email, this.password);
                let data = {
                    uname: this.uname,
                    password: this.password,
                };
                await this.$store.dispatch("login", data);
                this.$emit('close-dialog')
                if (this.$store.state.user.isHost) {
                    await router.push({name: 'HostRooms'})
                } else {
                    await router.push({name: 'Home'})
                }

            },
        }
    }
</script>

<style lang="css" scoped>
</style>
