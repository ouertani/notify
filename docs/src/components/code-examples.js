import React from 'react'
import styled, { css } from 'styled-components'
import { StaticQuery, graphql } from 'gatsby'
import SyntaxHighligher from './syntax-highlighter'

const linkCSS = css`
  line-height: 1.25;
  padding: 1.25rem 1.5rem;
  border-bottom: ${props =>
    props.active ? '0.35rem solid #007099' : '0.35rem solid #e0e0e0'};
  text-decoration: none;
  display: block;
  color: #007099;

  &:hover {
    color: #000;
    cursor: pointer;
  }
`

const Tabs = styled.div`
  margin-top: 1rem;
`

const TabsNav = styled.nav`
  border-bottom: 0.35rem solid #e0e0e0;
  width: 100%;
`

const Ul = styled.ul`
  margin: 0 0 -0.35rem;
  padding: 0;
  display: inline-block;
  line-height: 1.5;
  list-style-type: none;
`

const NavItem = styled.li`
  margin: 0;
  padding: 0;
  display: inline-block;
`

const NavLink = styled.a`
  ${linkCSS};
`

const TabContent = styled.div`
  display: ${props => (props.active ? 'block' : 'none')};
`

export const filterTransformSortCodeSnippets = ({ codeSnippets, path }) => {
  if (!codeSnippets) {
    return []
  }

  return codeSnippets
    .filter(n => n.node.relativePath.startsWith(path))
    .map(n => n.node)
    .sort((a, b) => a.name.localeCompare(b.name))
}

export class CodeExamplesComponent extends React.Component {
  state = {
    activeTab: 0,
  }

  handleClick = index => e => {
    e.preventDefault()
    this.setState({ activeTab: index })
  }

  render = () => {
    const codeSnippets = filterTransformSortCodeSnippets({
      codeSnippets: this.props.data.allCodeSamples.edges,
      path: this.props.path,
    })
    return (
      <Tabs>
        <TabsNav>
          <Ul>
            {codeSnippets.map((s, i) => (
              <NavItem key={s.id}>
                <NavLink
                  href=""
                  onClick={this.handleClick(i)}
                  active={this.state.activeTab === i}
                >
                  {s.name}
                </NavLink>
              </NavItem>
            ))}
          </Ul>
        </TabsNav>

        {codeSnippets.map((s, i) => (
          <TabContent key={s.id} active={this.state.activeTab === i}>
            <SyntaxHighligher content={s.content} language={s.extension} />
          </TabContent>
        ))}
      </Tabs>
    )
  }
}

export default ({ path }) => (
  <StaticQuery
    query={graphql`
      query {
        allCodeSamples {
          edges {
            node {
              id
              content
              extension
              relativePath
              name
            }
          }
        }
      }
    `}
    render={data => <CodeExamplesComponent data={data} path={path} />}
  />
)
