<template >
    <v-container  >
        <v-row   align="center" dense>
             <v-col >
                <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="dates"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"

                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        label="Select Dates"
                        readonly
                        style="max-width: 120px"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="dates" no-title scrollable range color="brown">
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                      <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                    </v-date-picker>
                  </v-menu>

            </v-col>
             <v-text-field
              v-model="persons"
              label="Persons"
              min="1"
              step="1"
              style="max-width: 50px"
              type="number"/>
            <v-col>
                <v-btn color="primary">

                Search
            </v-btn>
           </v-col>

            <v-col cols="2">
                <v-select :items="room_types"
                          outlined
                          dense
                          label="Room Type"
                            style="height: 40px"
                            >

                </v-select>

            </v-col>


            <v-col >
                <v-switch v-model="wifi" label=" Wifi ">

                </v-switch>

            </v-col>
             <v-col>
                <v-switch v-model="air_condition" label="A/C">

                </v-switch>

            </v-col>
             <v-col>
                <v-switch v-model="refrigerator" label="Refrigerator">

                </v-switch>

            </v-col>
             <v-col>
                <v-switch v-model="kitchen" label="Kitchen">

                </v-switch>

            </v-col>
             <v-col>
                <v-switch v-model="tv" label="TV">

                </v-switch>

            </v-col>
             <v-col>
                <v-switch v-model="parking" label="Parking">

                </v-switch>

            </v-col>

             <v-col>
                <v-switch v-model="elevator" label="Elevator">

                </v-switch>
            </v-col>
              <v-col cols="2">
                <v-select :items="order"
                          outlined
                          dense
                          label="Order By"
                            style="height: 40px"
                            >

                </v-select>

            </v-col>
        </v-row>
        <v-row >

        </v-row>

    </v-container>

</template>

<script>
    export default {
        name: "Options",
        data:function () {
            return {
                menu:false,
                room_types :['Private','shared','House'],
                wifi:true,
                air_condition:true,
                refrigerator:true,
                kitchen:true,
                tv:true,
                parking:true,
                elevator:true,
                 dates: [],
                persons:0,
                order:['Ascending price','Descending price']
            }

        }

    }
</script>

<style scoped>

</style>