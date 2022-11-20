const HOST = 'http://127.0.0.1:8000/api/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COLLECTIONS = 'collections/'
const COMMUNITY = 'commnunity/'
const GAMES = 'games/'


export default {
    accounts: {
        login: () => HOST + ACCOUNTS + 'login/',
        logout: () => HOST + ACCOUNTS + 'logout/',
        signup: () => HOST + ACCOUNTS + 'signup/',

        // Token 으로 현재 user 판단
        currentUserInfo: () => HOST + ACCOUNTS + 'currentuser/',

        // username으로 프로필 제공
        profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
        set_nickname: () => HOST + ACCOUNTS + 'profile/set_nickname/',
        set_message: () => HOST + ACCOUNTS + 'profile/' + 'set_message/',
        update_profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/update/`,
        followuser: user_pk => HOST + ACCOUNTS + 'profile/' + `${user_pk}/` + 'follow/',
        user_like_movies: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'movies/',
        user_reviews: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'reviews/',
        user_collections: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'collections/',
    },
    movies: {
        movies: () => HOST + MOVIES,
        movie: movie_pk => HOST + MOVIES + `${movie_pk}`,
        likeMovie: movie_pk => HOST + MOVIES + `${movie_pk}/` + 'like/',
        reviews: movie_pk => HOST + MOVIES + `${movie_pk}/` + 'reviews/',
        collections: movie_pk => HOST + MOVIES + `${movie_pk}/` + 'collections/',
        auto_complete: keyword => HOST + MOVIES + 'search/' + `${keyword}/`,
    },
    collections: {
        collection_list: () => HOST + COLLECTIONS,
        collection_create: () => HOST + COLLECTIONS + 'create/',
        collection_suggestions: keyword => HOST + COLLECTIONS + 'create/' + `${keyword}/`,
        collection_detail: collection_pk => HOST + COLLECTIONS + `${collection_pk}/`,
        collection_like: collection_pk => HOST + COLLECTIONS + `${collection_pk}/` + 'like/',
        collection_comments_create: collection_pk => HOST + COLLECTIONS + `${collection_pk}/` + 'comments/create/',
        collection_comments_status: (collection_pk, comment_pk) => HOST + COLLECTIONS + `${collection_pk}/` + 'comments/' + `${comment_pk}`,
    },
    games: {
        actorquiz: () => HOST + GAMES + 'actorquiz/',
        oxquiz: () => HOST + GAMES + 'oxquiz/',
        user_exp: user_pk => HOST + GAMES + `${user_pk}`
    },
    community: {
        review_list: () => HOST + COMMUNITY,
        search_review: movie_pk => HOST + COMMUNITY + `${movie_pk}/`,
        create_review:  movie_pk => HOST + COMMUNITY +  `${movie_pk}/` + 'create/',
        review_detail: (movie_pk, review_pk) => HOST + COMMUNITY + `${movie_pk}/` + `${review_pk}`,
        like_review: (movie_pk, review_pk) => HOST + COMMUNITY + `${movie_pk}/` + `${review_pk}` + 'like/',
        comments_list: (movie_pk, review_pk) => HOST + COMMUNITY + `${movie_pk}/` + `${review_pk}` + 'comments/',
        comment_statue: (movie_pk, review_pk, comment_pk) => HOST + COMMUNITY + `${movie_pk}/` + `${review_pk}` + 'comments/' + `${comment_pk}`,
    },
    }
