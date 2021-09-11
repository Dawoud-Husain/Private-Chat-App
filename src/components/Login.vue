<head>
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
</head>

<template>

  <div class="login">
    <div v-if="proccessing" class="text-center">Please wait...</div>
    <div v-if="message" class="text-center">{{ message }}</div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-6 col-md-6 form-container">
          <div
            class="col-lg-8 col-md-12 col-sm-9 col-xs-12 form-box text-center"
          >
            <div class="logo mt-5 mb-3">
              <img
                src="..\assets\image\conversation-3425922_1920.jpg"
                width="150px"
              />
            </div>

            <div class="heading mb-3">
              <h4>Login into your account</h4>
            </div>

            <form>
              <div class="form-input">
                <span><i class="fa fa-envelope"></i></span>
                <b-form-input
                  v-model="username"
                  type="text"
                  class="input-form"
                  placeholder="Username"
                >
                </b-form-input>
              </div>

              <div class="form-input">
                <b-form-input
                  v-model="password"
                  class="input-form"
                  type="password"
                  placeholder="Password"
                >
                </b-form-input>
              </div>

              <div class="text-left mb-3">
                <!-- <button type="submit" class="btn">Login</button> -->

                <b-button
                  v-on:click="login"
                  variant="primary"
                  class="btn-block"
                  
                >
                  Login
                </b-button>
              </div>
            </form>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 d-none d-md-block image-container"></div>
      </div>
    </div>
  </div>
</template>

<script>
// Export an object defining the username and password
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      proccessing: false,
      message: "",
    };
  },

  //  Make a POST request to /api/login to authenticate users 
  methods: {
    login: function() {
      this.loading = true;
      this.axios
        .post("/api/login", {
          username: this.username,
          password: this.password,
        })

        // If sucessfull emit an event named authenticated to act on in app.vue
        .then((response) => {
          if (response.data.status == "success") {
            this.proccessing = false;
            this.$emit("authenticated", true, response.data.data);
          } else {
            this.message = "Login Faild, try again";
          }
        })

        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.message = "Login Faild, try again";
          this.proccessing = false;
        });
    },
  },
};
</script>

<style scoped>
/* .login {
  width: 500px;
  border: 1px solid #cccccc;
  background-color: #ffffff;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
}
.input-form {
  margin-bottom: 9px;
} */

.image-container {

  background: url("../assets/image/earth-1149733.jpg") center no-repeat;
  background-size: cover;
  height: 100vh;
}

.form-container {
  background-color: #555555;
  display: flex;
  justify-content: center;
}

.form-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 100vh;
}

.form-box h4 {
  font-weight: bold;
  color: #fff;
}

.form-box .form-input {
  position: relative;
}

.form-box .form-input input {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  border: none;
  border-radius: 5px;
  outline: none;
  background: white;
  padding-left: 45px;
}

.form-box .form-input span {
  position: absolute;
  top: 8px;
  padding-left: 20px;
  color: #777;
}

.form-box .form-input input::placeholder {
  padding-left: 0px;
}

.form-box .form-input input:focus,
.form-box .form-input input:valid {
  border-bottom: 2px solid #dc3545;
}

.form-box button[type="submit"] {
  border: none;
  cursor: pointer;
  width: 150px;
  height: 40px;
  border-radius: 5px;
  background-color: #fff;
  color: #000;
  font-weight: bold;
  transition: 0.5s;
}

.form-box button[type="submit"]:hover {
  -webkit-box-shadow: 0px 9px 10px -2px rgba(0, 0, 0, 0.55);
  -moz-box-shadow: 0px 9px 10px -2px rgba(0, 0, 0, 0.55);
  box-shadow: 0px 9px 10px -2px rgba(0, 0, 0, 0.55);
}
</style>
