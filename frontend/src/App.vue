<template>
    <div class="row p-0">
        <div class="col col-12">
            <h1>Australian Jobs Market With Twitter Trends</h1>
            <p class="lead text-center">A analytic project for COMP90024.</p>
        </div>
    </div>
    <div id="app">
        <nav class="navbar navbar-expand-lg my-2" id="navbar">
            <div class="container">
                <a class="navbar-brand" href="/Home">Home Page</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                    <ul class="navbar-nav ms-auto ">
                        <li class="nav-item">
                            <a class="nav-link" href="/view0">Overview</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/RegionView">By Regions</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/TweetView">Tweets Analysis</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>

    <router-view> </router-view>


</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #161471;
    margin-top: 50px
}

img {
    height: 50px;
}

h1 {
    p {
        margin-bottom: 0;
    }
    font-size: 3.1em;
    color: #161471;
    font-weight: bold;
}

h2 {
    font-size: 2em;
    color: #161471;
    font-weight: bold;
}

h3 {
    font-size: 1.5em;
    color: #161471;
    font-weight: bold;
}

h4 {
    font-size: 1.25em;
    color: #161471;
    font-weight: bold;
}

</style>
