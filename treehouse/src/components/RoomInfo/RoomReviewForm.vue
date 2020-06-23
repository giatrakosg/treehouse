<template>
    <v-card>
        <ValidationObserver ref="observer">
            <v-container>
                <v-card-title>
                    Rating:
                    <ValidationProvider v-slot="{ errors }" rules="required">
                        <v-rating
                                half-increments
                                v-model="rating"
                                :error-messages="errors"

                        />
                    </ValidationProvider>
                </v-card-title>
                <v-card-subtitle>
                        <span v-if="rating===null"
                              style="color: #ff1744;font-size: 12px">Rating is required</span>
                </v-card-subtitle>

                <v-card-text>
                    <ValidationProvider v-slot="{ errors }" rules="required|max:50">
                        <v-text-field
                                v-model="title"
                                :counter="30"
                                maxlength="30"
                                :error-messages="errors"
                                label="Title"
                        ></v-text-field>
                    </ValidationProvider>
                    <ValidationProvider v-slot="{ errors }" rules="required">
                        <v-textarea
                                v-model="description"
                                label="Description"
                                :error-messages="errors"

                        >
                        </v-textarea>
                    </ValidationProvider>
                    <v-spacer/>


                </v-card-text>
            </v-container>

            <v-card-actions>
                <v-spacer/>

                <v-btn color="primary" @click="Submit">Submit</v-btn>
                <v-btn color="primary" text @click="Close">Close</v-btn>
            </v-card-actions>
        </ValidationObserver>
    </v-card>
</template>

<script>
    import {extend} from 'vee-validate';
    import {required, max} from "vee-validate/dist/rules";
    import {ValidationProvider, ValidationObserver} from 'vee-validate';

    extend('required', {
        ...required,
        message: 'This field is required'
    });
    extend('max', {
        ...max,
        message: '{_field_} may not be greater than {length} characters',
    });
    export default {
        props: ['room_title'],
        components: {
            ValidationProvider,
            ValidationObserver
        },
        name: "RoomReviewForm",
        data: () => ({

            title: '',
            description: '',
            rating: null,


        }),

        methods: {
            async Submit() {
                if (await this.$refs.observer.validate()) {

                    console.log(this.$store.state.user)


                    let new_review = {
                        title: this.title,
                        description: this.description,
                        rating: this.rating,
                        user_name: 'test',
                        user_id: 2

                    };
                    let room_id = this.$store.state.room.Id
                    await this.$store.dispatch('saveReview', {new_review, room_id})
                    this.Close()

                }
            },
            Clear() {
                this.title = '';
                this.description = '';
                this.rating = null;
                this.$refs.observer.reset()
            },
            Close() {
                this.Clear();
                this.$emit('close-review-form');

            }
        }
    }
</script>

<style scoped>

</style>