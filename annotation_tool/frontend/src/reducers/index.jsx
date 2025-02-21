import { combineReducers } from "redux";
import { reducer as formReducer } from "redux-form";
import model from "src/reducers/model";
import localState from "src/reducers/localState";
import codingProgressStore from "src/reducers/codingProgress";
import errorState from "src/reducers/errorState";
export const rootReducer = combineReducers({
  form: formReducer,
  model,
  localState,
  codingProgressStore,
  errors: errorState,
});
