import styled from "styled-components";

const Place = styled.select`
  flex: 1;
  max-width: 300px;
`;

const SearchBar = () => {
  return (
    <>
      <p>Location</p>
      <Place className="form-select form-select-lg">
        <option selected>Open this select menu</option>
        <option value="1">Singanallur</option>
        <option value="2">Sulur</option>
      </Place>
    </>
  );
};

export default SearchBar;
