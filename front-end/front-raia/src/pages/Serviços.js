import { Form } from "react-bootstrap";
import { api } from "../service/api";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Serviços = () => {
  const navigate = useNavigate();

  const [userEmail, setUserEmail] = useState("");
  const [userPassword, setUserPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await api.post("/login", {
      email: userEmail,
      password: userPassword,
    });

    // console.log(response.data);

    const accessToken = response.data.access_token;

    localStorage.setItem("token", accessToken);

    navigate("/");
  };

  return (
    <Form onSubmit={handleSubmit}>
      <input
        placeholder="Email"
        value={userEmail}
        onChange={(e) => setUserEmail(e.target.value)}
      />
      <input
        placeholder="Password"
        type="password"
        value={userPassword}
        onChange={(e) => setUserPassword(e.target.value)}
      />
      <button type="submit">Login</button>
    </Form>
  );
};
export default Serviços;
