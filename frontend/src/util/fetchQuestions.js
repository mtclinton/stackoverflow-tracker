import {BASE_API_URL} from '../constants';


const fetchQuestions = async (
    type,
    pageNumber,
)  => {
    try {
        let request = `${BASE_API_URL}/${type}${pageNumber}`;

        return fetch(request).then((response) => {
            return response.json().then((data) => {
                // console.log(data.message)
                return data.message;
                // return 'brapp';
            });
        });

    } catch (error) {
        console.log(error);
        return 0;
    }

};

export default fetchQuestions;