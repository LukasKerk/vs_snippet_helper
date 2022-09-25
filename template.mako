<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title>${title}</Title>
            <Shortcut>${shortcut}</Shortcut>
        </Header>
        <Snippet>
            <Declarations>
            % for var in variables:
              <Literal>
                <ID>${var}</ID>
                <Default>${var}</Default>
              </Literal>
            % endfor
            </Declarations>
            <Code Language="Cpp">
                <![CDATA[${text}]]>
            </Code>
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
