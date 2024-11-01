import { createApi } from "@reduxjs/toolkit/query/react";
import axios from "axios";

const baseQuery = ({ baseUrl }) => async({ path, method, data, params }) => {
  const {data: responseData, ...meta} =
    await axios({url: baseUrl + path, method, data, params})
  return { meta, data: responseData }
}

export const elsaSystemApi = createApi({
  reducerPath: 'elsaSystemApi',
  baseQuery: baseQuery()

})
