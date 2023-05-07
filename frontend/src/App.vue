<template>
    <div class="row p-0">
        <div class="col col-12">
            <h1>Australian Jobs Market With Twitter Trends</h1>
            <p class="lead text-center">A analytic project for COMP90024.</p>
        </div>
    </div>
    <div id="app">
        <nav class="navbar navbar-expand-lg my-2">
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
                            <a class="nav-link" href="/RegionView">Regions</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/IndustView">Industries</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/OccuView">Occupations</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/TweetView">Twitter Analysis</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>

    <router-view> </router-view>
<!--    <div class="row no-gutters">-->
<!--        <div class="col col-12">-->
<!--            <ul class="nav nav-tabs explore-bar-tabs" id="explore-bar-tabs">-->
<!--                <li class="nav-item explore-bar-tab">-->
<!--                    <a class="nav-link active d-flex align-items-center px-4" href="#" data-toggle="tab" data-ga-event="{&quot;eventName&quot;:&quot;RegionsExploreBarItemClick&quot;,&quot;eventParameters&quot;:{&quot;event_category&quot;:&quot;ExploreBarEvents&quot;,&quot;event_label&quot;:&quot;Regions&quot;}}" data-ga-event-force-location="true">-->
<!--                        <span class="region tab-icon"></span>-->
<!--                        <span class="pl-3">-->
<!--                            Regions-->
<!--                        </span>-->
<!--                    </a>-->
<!--                </li>-->
<!--                <li class="nav-item px-2 explore-bar-tab">-->
<!--                    <a class="nav-link d-flex align-items-center px-4" href="#" data-toggle="tab" data-ga-event="{&quot;eventName&quot;:&quot;IndustriesExploreBarItemClick&quot;,&quot;eventParameters&quot;:{&quot;event_category&quot;:&quot;ExploreBarEvents&quot;,&quot;event_label&quot;:&quot;Industries&quot;}}" data-ga-event-force-location="true">-->
<!--                        <span class="industry tab-icon"></span>-->
<!--                        <span class="pl-3">-->
<!--                            Industries-->
<!--                        </span>-->
<!--                    </a>-->
<!--                </li>-->
<!--                <li class="nav-item explore-bar-tab">-->
<!--                    <a class="nav-link d-flex align-items-center px-4" href="#" data-toggle="tab" data-ga-event="{&quot;eventName&quot;:&quot;OccupationsExploreBarItemClick&quot;,&quot;eventParameters&quot;:{&quot;event_category&quot;:&quot;ExploreBarEvents&quot;,&quot;event_label&quot;:&quot;Occupations&quot;}}" data-ga-event-force-location="true">-->
<!--                        <span class="occupation tab-icon"></span>-->
<!--                        <span class="pl-3">-->
<!--                            Occupations-->
<!--                        </span>-->
<!--                    </a>-->
<!--                </li>-->

<!--            </ul>-->
<!--        </div>-->
<!--    </div>-->


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
