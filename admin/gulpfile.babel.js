// GULPFILE
// - - - - - - - - - - - - - - -
// This file processes all of the assets in the "src" folder
// and outputs the finished files in the "dist" folder.

// 1. LIBRARIES
// - - - - - - - - - - - - - - -
import gulp from "gulp";
import loadPlugins from "gulp-load-plugins";
import sourcemaps from "gulp-sourcemaps";
import stylish from "jshint-stylish";
import { argv } from "yargs";

const throwInProduction = argv.production
  ? err => {
      throw new Error(err.message);
    }
  : undefined;

const plugins = loadPlugins(),
  // 2. CONFIGURATION
  // - - - - - - - - - - - - - - -
  paths = {
    src: "app/assets/",
    dist: "app/static/",
    npm: "node_modules/",
    template: "node_modules/govuk_template_jinja/",
    toolkit: "node_modules/govuk_frontend_toolkit/"
  };

// 3. TASKS
// - - - - - - - - - - - - - - -

// Move govuk-template resources

gulp.task("copy:govuk_template:css", () =>
  gulp
    .src(paths.template + "assets/stylesheets/**/*.css")
    .pipe(plugins.prettyerror(throwInProduction))
    .pipe(
      plugins.sass({
        outputStyle: "compressed"
      })
    )
    .pipe(
      plugins.cssUrlAdjuster({
        prependRelative: "/static/"
      })
    )
    .pipe(gulp.dest(paths.dist + "stylesheets/"))
);

gulp.task("copy:govuk_template:js", () =>
  gulp
    .src(paths.template + "assets/javascripts/**/*.js")
    .pipe(plugins.uglify())
    .pipe(gulp.dest(paths.dist + "javascripts/"))
);

gulp.task("copy:govuk_template:images", () =>
  gulp
    .src([
      `${paths.template}assets/stylesheets/images/**/*`,
      `!${paths.template}assets/stylesheets/images/govuk*`,
      `!${paths.template}assets/stylesheets/images/gov.uk*`
    ])
    .pipe(gulp.dest(paths.dist + "images/"))
);

gulp.task("javascripts", () =>
  gulp
    .src([
      paths.src + "javascripts/sentry.js",
      paths.toolkit + "javascripts/govuk/modules.js",
      paths.src + "javascripts/stick-to-window-when-scrolling.js",
      paths.src + "javascripts/detailsPolyfill.js",
      paths.src + "javascripts/apiKey.js",
      paths.src + "javascripts/autofocus.js",
      paths.src + "javascripts/highlightTags.js",
      paths.src + "javascripts/fileUpload.js",
      paths.src + "javascripts/expandCollapse.js",
      paths.src + "javascripts/radioSelect.js",
      paths.src + "javascripts/updateContent.js",
      paths.src + "javascripts/listEntry.js",
      paths.src + "javascripts/liveSearch.js",
      paths.src + "javascripts/errorTracking.js",
      paths.src + "javascripts/preventDuplicateFormSubmissions.js",
      paths.src + "javascripts/fullscreenTable.js",
      paths.src + "javascripts/main.js"
    ])
    .pipe(plugins.prettyerror(throwInProduction))
    .pipe(sourcemaps.init())
    .pipe(
      plugins.babel({
        presets: ["es2015"],
        plugins: [
          [
            "transform-inline-environment-variables",
            {
              include: ["ADMIN_SENTRY_DSN", "ADMIN_SENTRY_ENV", "CIRCLE_SHA1"]
            }
          ]
        ]
      })
    )
    .pipe(
      plugins.addSrc.prepend([
        paths.npm + "@sentry/browser/build/bundle.min.js",
        paths.npm + "hogan.js/dist/hogan-3.0.2.js",
        paths.npm + "jquery/dist/jquery.min.js",
        paths.npm + "jquery-migrate/dist/jquery-migrate.min.js",
        paths.npm + "query-command-supported/dist/queryCommandSupported.min.js",
        paths.npm + "diff-dom/diffDOM.js",
        paths.npm + "timeago/jquery.timeago.js",
        paths.npm + "textarea-caret/index.js"
      ])
    )
    .pipe(plugins.uglify())
    .pipe(plugins.concat("all.js"))
    .pipe(sourcemaps.write("../maps/"))
    .pipe(gulp.dest(paths.dist + "javascripts/"))
);

gulp.task("sass", () =>
  gulp
    .src(paths.src + "/stylesheets/main*.scss")
    //.pipe(plugins.prettyerror(() => { throw new Error('welp') }))
    .pipe(plugins.prettyerror(throwInProduction))
    .pipe(
      plugins.sass({
        outputStyle: "compressed",
        includePaths: [
          paths.npm + "govuk-elements-sass/public/sass/",
          paths.toolkit + "stylesheets/"
        ]
      })
    )
    .pipe(plugins.base64({ baseDir: "app" }))
    .pipe(gulp.dest(paths.dist + "stylesheets/"))
);

// Copy images

gulp.task("images", () =>
  gulp
    .src([
      `${paths.src}images/**/*`,
      `${paths.toolkit}images/**/*`,
      `${paths.template}assets/images/**/*`,
      `!${paths.template}assets/images/gov.uk*`,
      `!${paths.template}assets/images/favicon*`,
      `!${paths.template}assets/images/apple-touch-icon*.png`
    ])
    .pipe(gulp.dest(paths.dist + "images/"))
);

gulp.task("copy:govuk_template:error_page", () =>
  gulp
    .src(paths.src + "error_pages/**/*")
    .pipe(gulp.dest(paths.dist + "error_pages/"))
);

gulp.task("copy:misc", () =>
  gulp
    .src([paths.src + "manifest.json", paths.src + "browserconfig.xml"])
    .pipe(gulp.dest(paths.dist))
);

// Watch for changes and re-run tasks
gulp.task("watchForChanges", function() {
  gulp.watch(paths.src + "javascripts/**/*", gulp.series("javascripts"));
  gulp.watch(paths.src + "stylesheets/**/*", gulp.series("sass"));
  gulp.watch(paths.src + "images/**/*", gulp.series("images"));
  gulp.watch("gulpfile.babel.js", gulp.series("default"));
});

gulp.task("lint:js", () =>
  gulp
    .src(paths.src + "javascripts/**/*.js")
    .pipe(plugins.jshint())
    .pipe(plugins.jshint.reporter(stylish))
    .pipe(plugins.jshint.reporter("fail"))
);

gulp.task("lint", gulp.series("lint:js"));

// Default: compile everything
gulp.task(
  "default",
  gulp.series(
    "copy:govuk_template:images",
    //'copy:govuk_template:css',
    "copy:govuk_template:js",
    "copy:govuk_template:error_page",
    "copy:misc",
    "javascripts",
    "sass",
    "images"
  )
);

// Optional: recompile on changes
gulp.task("watch", gulp.series("default", "watchForChanges"));
