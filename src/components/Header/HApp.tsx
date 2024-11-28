import DateOption from "./DateOption";
import SearchBar from "./SearchBar";
import styled from "styled-components";
import SearchBtn from "./SearchBtn";

const Flex = styled.div`
  padding: 10px;
  margin: 10px;
  width: 700px;
  background-color: aliceblue;

  display: flex;
  align-items: center;
  justify-content: space-around;
`;

const HApp = () => {
  return (
    <Flex id="Header">
      <SearchBar />
      <SearchBtn />
      <DateOption />
    </Flex>
  );
};

export default HApp;
