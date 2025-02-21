import React from "react";
import { PROJECT_NAME } from "src/constants";
export default function Heading({ coder_email, title }) {
  const home_url = document.location.pathname.startsWith("/c/") ? `/c/${PROJECT_NAME}/` : '/';
  const back_url = location.pathname == "/c/" ? "/" : "..";
  return (
    <div id="title">
      <div>
        <h1>
          <span style={{ fontSize: "1.3em", marginRight: ".5em" }}>
            📋
          </span>
          {title} </h1>
      </div>
      <div>
        <a href={`${back_url}`}>back</a>
        <a href={`${home_url}`}>home</a>
        <a href="/accounts/logout">logout</a>
      </div>
    </div >
  );
}
