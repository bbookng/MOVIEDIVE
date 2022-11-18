const HOST = 'http://localhost:8000/api/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COLLECTIONS = 'collections/'
const COMMUNITY = 'commnunity/'


export default {
    accounts: {
        login: () => HOST + ACCOUNTS + 'login/',
        logout: () => HOST + ACCOUNTS + 'logout/',
        signup: () => HOST + ACCOUNTS + 'signup/',

        // Token 으로 현재 user 판단
        currentUserInfo: () => HOST + ACCOUNTS + 'currentuser/',

        // username으로 프로필 제공
        profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
        set_nickname: () => HOST + ACCOUNTS + 'profile/' + 'set_nickname/',
        set_message: () => HOST + ACCOUNTS + 'profile/' + 'set_message/',
        update_profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/update/`,
        followuser: userPk => HOST + ACCOUNTS + 'profile/' + `${user_pk}/` + 'follow/',
        user_like_movies: username => POST + ACCOUNTS + 'profile/' + `${username}/` + 'movies/',
        user_reviews: username => POST + ACCOUNTS + 'profile/' + `${username}/` + 'reviews/',
        user_collections: username => POST + ACCOUNTS + 'profile/' + `${username}/` + 'collections/',
    },
    movies: {
        movies: () => HOST + MOVIES,
        movie: moviePk => HOST + MOVIES + `${moviePk}`,
        wishMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'wish/',
        review: moviePk => HOST + MOVIES + `${moviePk}/` + 'review/',
        reviews: moviePk => HOST + MOVIES + `${moviePk}/` + 'reviews/',
        likeUpDeReview: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'reviews/' + `${reviewPk}`,
        //   HOST + MOVIES + `${articlePk}/` + REVIEWS + `${commentPk}/`,
        auto_complete: keyword => HOST + MOVIES + 'search/' + `${keyword}/`,
        lookForCollections: moviePk => HOST + MOVIES + `${moviePk}/` + 'collections/'
    },
    collections: {
        main_collections: () => HOST + COLLECTIONS +  'main',
        collection_list: () => HOST + COLLECTIONS,
        collection_list_orderby: () => HOST + 'collections',
        collection_detail: collectionPk => HOST + COLLECTIONS + `${collectionPk}/`,
        like_collection: collectionPk => HOST + COLLECTIONS + `${collectionPk}/` + LIKE,
    },
    bingos: {
        current_bingo: () => HOST + BINGOS + 'current',
    },
    community: {
        community_list: () => HOST + COMMUNITY,
        create_thread: moviePk => HOST + COMMUNITY + `create/${moviePk}/`,

        thread_detail: threadPk => HOST + COMMUNITY + `${threadPk}`,
        create_comment: threadPk => HOST + COMMUNITY + `${threadPk}/` + 'comment/',
        delete_comment: (threadPk, commentPk) => HOST + COMMUNITY + `${threadPk}/` + 'comment/' +`${commentPk}/`,
        checkThread: moviePk => HOST + COMMUNITY + 'moviethread/' + `${moviePk}/`
    }
    }
