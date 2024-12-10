<template>
    <div class="body">
        <div class="login-container">
        <div class="login-box">
            <h1>Login</h1>
            <form>
                <div class="input-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" placeholder="Enter your username">
                </div>
                <div class="input-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" placeholder="Enter your password">
                </div>
                <button type="submit" class="login-button">Login</button>
            </form>
        </div>
    </div>
    </div>


</template>


<script>
export default {
  name: 'TheLogin',
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(to bottom, #1a1a2e, #16213e);
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
  }
 .login-container {
            width: 100%;
            max-width: 400px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
}


.login-box h1 {
    text-align: center;
    font-size: 2em;
    margin-bottom: 20px;
}


.input-group {
    margin-bottom: 15px;
}


.input-group label {
    display: block;
    margin-bottom: 5px;
    font-size: 0.9em;
    color: #aaa;
}


.input-group input {
    width: 100%;
    max-width: 380px;
    padding: 10px;
    font-size: 1em;
    border: none;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.2);
    color: #fff;
    outline: none;
}


.input-group input::placeholder {
    color: #bbb;
}


.login-button {
    width: 100%;
    padding: 10px;
    font-size: 1em;
    background: linear-gradient(to right, #4e54c8, #8f94fb);
    color: #fff;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s;
}


.login-button:hover {
    background: linear-gradient(to right, #8f94fb, #4e54c8);
}
</style>