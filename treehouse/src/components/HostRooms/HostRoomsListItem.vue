<template>
     <v-list-item to="/hostroomedit" v-on:mouseover="$root.$emit('highlight',$vnode.key)"
                  v-on:mouseleave="$root.$emit('default',$vnode.key)" ref="room">
         <v-list-item-avatar tile size="180px">


             <v-img style="border-radius: 8px" src="../../assets/back-ground-image-3.jpg">

             </v-img>

         </v-list-item-avatar>

         <v-list-item-content>
            <v-list-item-title>

                    <h3 style="display: inline-flex">Awesome Room</h3>

            </v-list-item-title>
            <v-list-item-subtitle >

                 <v-chip color="blue" style="color:white " v-ripple="false">
                    <i class="fas fa-euro-sign fa-lg"></i>
                    <label style="font-size: 16px;" > /day:12</label>
                </v-chip>
               <v-chip-group column class="hidden-md-and-down">
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-shower</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px;"> 12</label>
                            </v-chip>
                        </template>
                        Bathrooms number :12
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-on="on" v-ripple="false">
                                <v-icon>mdi-bed-king</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px;">2</label>
                            </v-chip>
                        </template>
                        Bedrooms number :2
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <label style="font-size: 16px;">Room type</label>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <v-icon>mdi-account</v-icon>
                            </v-chip>
                        </template>
                        Private Room
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-bed</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">2</label>
                            </v-chip>
                        </template>
                        Beds number :2
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-sofa</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Lounge
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-fit-to-page</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">12 m<sup>2</sup> </label>
                            </v-chip>
                        </template>
                        Area
                    </v-tooltip>
                </v-chip-group>
                <v-chip-group column class="hidden-xs-only">
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip color="brown" style="color: white" v-ripple="false" v-on="on">
                                <v-icon>mdi-smoking</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Smocking Allowed
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-on="on" v-ripple="false">
                                <v-icon>mdi-paw</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-times-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Pets
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-ripple="false" v-on="on">
                                <v-icon>mdi-party-popper</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Events
                    </v-tooltip>

                    <v-chip top color="brown" style="color: white" v-ripple="false">
                        <label style="font-size: 16px">Minimum stay</label>
                        <span style="margin-left: 3px;margin-right: 3px">:</span>
                        <label style="font-size: 16px">2 days</label>
                    </v-chip>

                </v-chip-group>
            </v-list-item-subtitle>

        </v-list-item-content>

    </v-list-item>
</template>

<script>
    export default {
        name: "HostRoomsListItem",
        props: ['title', 'cost', 'description'],
        data: () => ({}),


    }
</script>

<style scoped>

</style>