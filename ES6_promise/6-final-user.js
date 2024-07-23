import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      const answerArray = [];
      results.forEach((promise) => {
        answerArray.push({
          status: promise.status,
          value: promise.status === 'fulfilled' ? promise.value : `${promise.reason.name}: ${promise.reason.message}`,
        });
      });
      return answerArray;
    });
}
