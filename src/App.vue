<template>
  <div id="app">
    <Login />
    <b-container>
      <NavBar :logged_user="logged_user_username" />
      <b-row class="main-area">
        <b-col cols="4" class="users">
          <Users />
        </b-col>
        <b-col cols="8" class="messages-area">
          <div class="messages-main">
            <div v-if="!current_chat_channel" class="select-chat text-center">
              <p>Select a user to start chatting...</p>
            </div>
            <Messages
              v-else
              :active_chat="active_chat_id"
              :messages="messages[current_chat_channel]"
            />
          </div>
          <MessageInput />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// import MessageInput from "@/components/MessageInput.vue";
// import Messages from "@/componenets/Messages.vue";
// import NavBar from "@/componenets/NavBar.vue";
// import Login from "@/components/Login.vue";
// import Users from "@/components/Users.vue";

import MessageInput from "./components/MessageInput.vue";
import Messages from "./components/Messages.vue";
import NavBar from "./components/NavBar.vue";
import Login from "./components/Login.vue";
import Users from "./components/Users.vue";

// eslint-disable-next-line no-unused-vars
import Pusher from "pusher-js";

// Pusher Varible
// eslint-disable-next-line no-unused-vars
let pusher;
export default {
  name: "app",
  components: {
    MessageInput,
    NavBar,
    Messages,
    Users,
    Login
  },

  data: function() {
    return {
      message: "Some Message"
    };
  },

  methods: {}
};
</script>

<!-- <style lang="scss"> -->
// @import "~@/assets/scss/vendors/bootstrap-vue/index"; // @import
"~@/assets/scss/vendors/bootstrap-vue/index"; // .messages-main { // overflow-y:
scroll; // height: 90%; // } // users { // padding: 0px !important; // border:
1px solid grey; // } // .no-margin { // margin: 0px; // } // .messages-area { //
border: 1px solid grey; // padding: 0px !important; // max-height:
calc(100vh-4em) !important; // } // .input-message { // height: 40px; // } //
.active { // background: #17a2b8 !important; // border: #17a2b8 !important; // }
// .main-area { // margin: 0px; // min-height: calc(100vh -5em) !important; // }
// .loggged_user { // color: white; // } // #app { // font-family: Avenir,
Helvetica, Arial, sans-serif; // -webkit-font-smoothing: antialiased; //
-moz-osx-font-smoothing: grayscale; // text-align: center; // color: #2c3e50; //
margin-top: 60px; // }

<style>
.messages-main {
  overflow-y: scroll;
  height: 90%;
}
.users {
  padding: 0px !important;
  border: 1px solid gray;
}
.no-margin {
  margin: 0px;
}
.messages-area {
  border: 1px solid gray;
  padding: 0px !important;
  max-height: calc(100vh - 4em) !important;
}
.input-message {
  height: 40px;
}
.active {
  background: #17a2b8 !important;
  border: #17a2b8 !important;
}
.select-chat {
  margin-top: 35vh;
  padding: 8px;
}
.main-area {
  margin: 0px;
  min-height: calc(100vh - 5em) !important;
}
.logged_user {
  color: white;
}
</style>
