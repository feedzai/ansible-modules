# Ansible Modules

[![Build Status](https://travis-ci.com/feedzai/ansible-modules.svg?branch=master)](https://travis-ci.com/feedzai/ansible-modules)

Feedzai collection of non core Ansible modules.

## How-to

Following the [directory layout best practices][1] these modules should go in the `library` folder of the root.

### Maven

Add dependency (to `pom.xml`):

```xml
<dependency>
    <groupId>com.feedzai.ansible</groupId>
    <artifactId>ansible-modules</artifactId>
    <version>${ansible-modules.version}</version>
    <classifier>dist</classifier>
    <type>tar.gz</type>
</dependency>
```

Using `maven-assembly-plugin` you can unpack the dependency in the desired folder (in `dist.xml`):

```xml
<dependencySet>
    <useProjectArtifact>false</useProjectArtifact>
    <useTransitiveDependencies>false</useTransitiveDependencies>
    <outputDirectory>library</outputDirectory>
    <unpack>true</unpack>
    <includes>
        <include>com.feedzai.ansible:ansible-modules</include>
    </includes>
</dependencySet>
```

[1]: https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html
