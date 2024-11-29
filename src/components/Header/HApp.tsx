import DateOption from "./HeadComponents/DateOption";
import SearchBar from "./HeadComponents/SearchBar";
import styled from "styled-components";
import SearchBtn from "./HeadComponents/SearchBtn";

//Common Style for both divs
const FlexType = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-around;
`;

const HeadContainer = styled(FlexType)`
  margin-top: 60px;
  flex-direction: column;
`;

const Flex = styled(FlexType)`
  padding: 10px;
  margin: 10px;
  width: 40%;
`;

const HApp = () => {
  return (
    <HeadContainer>
      <h1>Parking Space Availability</h1>
      <Flex id="Header">
        <SearchBar />
        <SearchBtn />
        <DateOption />
      </Flex>
    </HeadContainer>
  );
};

export default HApp;
