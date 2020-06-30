<template>
    <div class="home">
        <v-container fluid class="pa-0">
            <v-img
                    src="../assets/back-ground-image-3.jpg"
                    max-height="100vh">
                <v-row style="margin-top: 200px">

                    <v-spacer></v-spacer>

                    <v-col cols="7">
                        <HomeSearchForm/>
                    </v-col>
                    <v-spacer></v-spacer>
                </v-row>
                <v-row v-if="isLoggedIn">
                    <v-spacer></v-spacer>
                    <v-col cols="7">
                        <RecsCarousel />
                    </v-col>
                    <v-spacer></v-spacer>
                </v-row>
            </v-img>
        </v-container>
    </div>
</template>

<script>
    import HomeSearchForm from '../components/HomeSearchForm/HomeSearchForm'
    import RecsCarousel from '../components/Recommendations/RecsCarousel'
    export default {
        name: 'Home',
        components: {
            HomeSearchForm,
            RecsCarousel
        },
        computed : {
            isLoggedIn() {
                return this.$store.state.isLoggedIn;
            },
        }
    }
</script>
