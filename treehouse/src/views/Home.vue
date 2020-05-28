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
            </v-img>
        </v-container>
    </div>
</template>

<script>
    import HomeSearchForm from '../components/HomeSearchForm/HomeSearchForm'

    export default {
        name: 'Home',
        components: {
            HomeSearchForm
        }
    }
</script>
