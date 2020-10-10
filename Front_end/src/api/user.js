import { userApi } from "./index";
import { axios } from "@/utils/request";
import qs from "qs";

/**
 * @description: login func
 * @param parameter: {
 *          username: '',
 *          password: ''
 *        }
 * @param parameter
 * @returns {*}
 */

export function Login(parameter) {
  return axios({
    url: userApi.Login,
    method: "post",
    data: qs.stringify(parameter)
  });
}
